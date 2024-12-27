import numpy as np
import pandas as pd
from scipy.stats import skew

def calculate_psi_doane_bins(expected, actual):
    """
    Calculate the Population Stability Index (PSI) using Doane's rule for binning.
    
    Args:
        expected (array-like): Expected distribution.
        actual (array-like): Actual distribution.
    
    Returns:
        float: PSI value.
    """
    # Calculate the number of bins using Doane's rule
    n = len(expected)
    g1 = skew(expected)  # Skewness of the expected data
    k = int(1 + np.log2(n) + np.log2(1 + abs(g1) / np.sqrt(6 / n)))
    
    # Create bin edges using equal-width bins
    bin_edges = np.linspace(min(min(expected), min(actual)), max(max(expected), max(actual)), k + 1)
    
    # Digitize the data into bins
    expected_bins = np.digitize(expected, bin_edges, right=True)
    actual_bins = np.digitize(actual, bin_edges, right=True)
    
    # Calculate percentage of observations in each bin
    expected_perc = np.array([np.sum(expected_bins == i) for i in range(1, k + 1)]) / len(expected)
    actual_perc = np.array([np.sum(actual_bins == i) for i in range(1, k + 1)]) / len(actual)
    
    # Avoid division by zero and log(0) by adding a small value
    expected_perc = np.where(expected_perc == 0, 0.0001, expected_perc)
    actual_perc = np.where(actual_perc == 0, 0.0001, actual_perc)
    
    # Calculate PSI
    psi = np.sum((expected_perc - actual_perc) * np.log(expected_perc / actual_perc))
    
    return psi, k

# Example usage
expected_data = np.random.normal(50, 10, 1000)  # Expected data
actual_data = np.random.normal(52, 15, 1000)    # Actual data
psi_value, num_bins = calculate_psi_doane_bins(expected_data, actual_data)
print(f"PSI using Doane's rule: {psi_value:.4f}, Number of bins: {num_bins}")
