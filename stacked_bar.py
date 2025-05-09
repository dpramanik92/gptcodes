import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Type1': [10, 15, 20],
    'Type2': [5, 10, 15]
})

df.set_index('Category', inplace=True)

# Create subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot stacked bar chart
bars = df.plot(kind='bar', stacked=True, ax=ax, colormap='tab20c')

# Add value labels on each bar segment
for container in bars.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0:
            ax.annotate(
                f'{int(height)}',                      # Label
                (bar.get_x() + bar.get_width() / 2,   # X position
                 bar.get_y() + height / 2),           # Y position (center of segment)
                ha='center', va='center', fontsize=9, color='white'
            )

# Add total values at the top
totals = df.sum(axis=1)
for i, total in enumerate(totals):
    ax.annotate(
        f'Total: {int(total)}',
        (i, total),
        ha='center', va='bottom', fontsize=9, fontweight='bold'
    )

# Axis labels and title
ax.set_title('Stacked Bar Chart with Values & Totals')
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
