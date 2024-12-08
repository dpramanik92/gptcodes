import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'marks': [2, 4, 3, 4, 5, 3, 4, 3, 2, 2, 3, 3, 3, 3, 4, 5, 3, 3, 1]}
df = pd.DataFrame(data)

# Count the occurrences of each mark
mark_counts = df['marks'].value_counts().sort_index()

# Define unique colors for each bar
colors = ['#753734', '#ccae54', '#c2e394', '#628548', '#273b19']

# Plotting
fig,ax = plt.subplots(figsize=(5, 3))
bars = ax.bar(mark_counts.index, mark_counts.values, color=colors,width=0.9)

# Adding count above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # x-coordinate (center of bar)
        height,                            # y-coordinate (top of bar)
        f'{height}',                       # Text to display
        ha='center', va='bottom', fontsize=12  # Text alignment
    )

# Title and labels
plt.title("Count")
# ax.set_xlabel("Marks")
# ax.set_ylabel("Count")
ax.set_xticks(mark_counts.index)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
