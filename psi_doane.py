import numpy as np
import pandas as pd

def calculate_psi(actual, expected, bins=10, is_categorical=False):
    """
    Calculate the Population Stability Index (PSI) between two distributions.

    Parameters:
    - actual: array-like, baseline distribution
    - expected: array-like, comparison distribution
    - bins: int, number of bins (only for numerical data)
    - is_categorical: bool, whether the data is categorical

    Returns:
    - psi: float, the PSI value
    """
    if is_categorical:
        # For categorical data, get unique categories
        categories = list(set(actual) | set(expected))
        
        # Calculate proportions for each category
        actual_counts = pd.Series(actual).value_counts(normalize=True).reindex(categories, fill_value=0)
        expected_counts = pd.Series(expected).value_counts(normalize=True).reindex(categories, fill_value=0)
        
    else:
        # For numerical data, define bin edges using the actual distribution
        bin_edges = np.linspace(np.min(actual), np.max(actual), bins + 1)
        
        # Calculate proportions for each bin in both distributions
        actual_counts, _ = np.histogram(actual, bins=bin_edges)
        expected_counts, _ = np.histogram(expected, bins=bin_edges)
        
        # Convert counts to proportions
        actual_counts = actual_counts / len(actual)
        expected_counts = expected_counts / len(expected)
    
    # Avoid division by zero and log of zero
    actual_proportions = np.where(actual_counts == 0, 1e-8, actual_counts)
    expected_proportions = np.where(expected_counts == 0, 1e-8, expected_counts)
    
    # Calculate PSI for each category/bin
    psi_values = (actual_proportions - expected_proportions) * np.log(actual_proportions / expected_proportions)
    
    # Sum up PSI values for the total PSI
    psi = np.sum(psi_values)
    return psi

# Example usage

# Numerical example
actual_num = np.random.normal(50, 10, 1000)  # Baseline distribution
expected_num = np.random.normal(52, 12, 1000)  # Comparison distribution

psi_num = calculate_psi(actual_num, expected_num, bins=10, is_categorical=False)
print(f"Numerical PSI: {psi_num:.4f}")

# Categorical example
actual_cat = np.random.choice(['A', 'B', 'C', 'D'], size=1000, p=[0.4, 0.3, 0.2, 0.1])
expected_cat = np.random.choice(['A', 'B', 'C', 'D'], size=1000, p=[
