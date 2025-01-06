import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data
data = {
    'Category': ['A', 'B', 'C'],
    'Col1': [10, 15, 20],
    'Col2': [5, 10, 15],
    'Col3': [8, 12, 18],
    'Col4': [6, 9, 14]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Extract values for plotting
categories = df['Category']
x = np.arange(len(categories))  # X positions
width = 0.4  # Width of the bars

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# First stack (Col1 + Col2)
bar1 = ax.bar(x, df['Col1'], width, label='Col1')
bar2 = ax.bar(x, df['Col2'], width, bottom=df['Col1'], label='Col2')

# Second stack (Col3 + Col4)
bar3 = ax.bar(x + width + 0.1, df['Col3'], width, label='Col3')
bar4 = ax.bar(x + width + 0.1, df['Col4'], width, bottom=df['Col3'], label='Col4')

# Add total numbers between the bars
for i in range(len(categories)):
    # Calculate totals
    total_stack1 = df['Col1'][i] + df['Col2'][i]
    total_stack2 = df['Col3'][i] + df['Col4'][i]
    
    # Add text between the bars
    ax.text(x[i], total_stack1 + 1, str(total_stack1), ha='center', va='bottom', fontsize=10)
    ax.text(x[i] + width + 0.1, total_stack2 + 1, str(total_stack2), ha='center', va='bottom', fontsize=10)

# Customization
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart with Totals')
ax.set_xticks(x + width / 2 + 0.05)
ax.set_xticklabels(categories)
ax.legend()

# Show plot
plt.tight_layout()
plt.show()
