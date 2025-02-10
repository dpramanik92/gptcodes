import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

df = pd.read_excel("sample_data.xlsx")
distance = 4.5
whites = []
for i in range(len(df)):
    whites.append(distance-np.sum(df.iloc[i,1:])/2)


df.insert(1,"white",whites)

df = df[::-1]

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Create figure
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(8, 8)  

# Top half (Unequal widths)
ax1 = fig.add_subplot(gs[0:4, :3])  # Smaller width (Left)
ax2 = fig.add_subplot(gs[0:4, 2:])  # Larger width (Right)

# Bottom half (Equal widths)
ax3 = fig.add_subplot(gs[4:, 0:4])
ax4 = fig.add_subplot(gs[4:, 4:])

# Hide axes for top subplots
ax1.axis("off")
# Hide y-axis line (spine) but keep the y-ticks
ax2.spines["left"].set_visible(False)  # Hide left spine (y-axis line)
ax2.spines["right"].set_visible(False)  # Hide right spine (optional)
ax2.spines["top"].set_visible(False)  # Hide top spine (optional)
ax2.spines["bottom"].set_visible(False)  # Hide bottom spine (optional)

# Keep y-axis tick labels visible
ax2.tick_params(axis="y", which="both", length=0)  # Removes tick marks but keeps labels

# Hide x-axis completely (optional)
ax2.get_xaxis().set_visible(False)

categories = df["Name"]
bar_widths = np.array(df.iloc[:, 1:])  # Get numerical columns for stacking
colors = ["white","#1f77b4", "#ff7f0e", "#2ca02c"]  # Colors for the stacks
left_positions = np.zeros(len(categories))  # Initial positions (start at zero)

for i in range(bar_widths.shape[1]):
    bars = ax2.barh(categories, bar_widths[:, i], left=left_positions, color=colors[i], label=df.columns[i + 1],height = 0.8)

        # Add text inside bars in white
    for bar, value in zip(bars, bar_widths[:, i]):
        if value >0:
            ax2.text(
                bar.get_x() + bar.get_width() / 2,  # X position (middle of bar)
                bar.get_y() + bar.get_height() / 2,  # Y position (middle of bar)
                int(value),  # Text content
                ha="center", va="center", color="white", fontsize=10, fontweight="bold"
            )
        
    left_positions += bar_widths[:, i]  # Update left positions for stacking

# Override the 1st tick label (assuming it's at the bottom)
yticks = ax2.get_yticks()  # Get tick positions
yticklabels = categories.copy()  # Copy existing labels
yticklabels[0] = "XYZ"  # Replace the first tick with "XYZ"

# Apply the modified y-tick labels
ax2.set_yticks(yticks)
ax2.set_yticklabels(yticklabels)


# Get legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Sort legend labels alphabetically
sorted_pairs = sorted(zip(labels, handles))  # Sort based on labels
sorted_labels, sorted_handles = zip(*sorted_pairs)  # Unzip into separate lists

# Apply sorted legend
ax.legend(sorted_handles, sorted_labels, loc="upper right")


# Remove top and right spines for bottom subplots
for ax in [ax3, ax4]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Add a main title for the whole page
fig.suptitle("Custom Subplot Layout with Hidden Axes & Spines", fontsize=16)

# Titles for individual subplots
ax1.set_title("Smaller Subplot (Top Left)", fontsize=12,x=0.3)
ax2.set_title("Larger Subplot (Top Right)", fontsize=12)
ax3.set_title("Equal Subplot 1 (Bottom Left)", fontsize=12)
ax4.set_title("Equal Subplot 2 (Bottom Right)", fontsize=12)

# Show the layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
plt.show()
