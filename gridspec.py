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
ax2.axis("off")

# Remove top and right spines for bottom subplots
for ax in [ax3, ax4]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Add a main title for the whole page
fig.suptitle("Custom Subplot Layout with Hidden Axes & Spines", fontsize=16, fontweight='bold')

# Titles for individual subplots
ax1.set_title("Smaller Subplot (Top Left)", fontsize=12)
ax2.set_title("Larger Subplot (Top Right)", fontsize=12)
ax3.set_title("Equal Subplot 1 (Bottom Left)", fontsize=12)
ax4.set_title("Equal Subplot 2 (Bottom Right)", fontsize=12)

# Show the layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
plt.show()
