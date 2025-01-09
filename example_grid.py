import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Helper function to create a donut chart with adjustable radius
def create_donut(ax, data, labels, colors, title, radius):
    wedges, _ = ax.pie(
        data,
        labels=labels,
        colors=colors,
        radius=radius,
        wedgeprops=dict(width=radius * 0.3)  # Adjusting donut thickness relative to radius
    )
    ax.set_title(title, fontsize=12)

# Helper function to create a bar chart
def create_bar_chart(ax, data, labels, title):
    ax.bar(labels, data, color='#66c2a5', edgecolor='black')
    ax.set_title(title, fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(left=False, bottom=False)

# Data for donut charts
data1 = [30, 70]
data2 = [50, 50]
data3 = [20, 80]

# Data for bar charts
bar_data1 = [5, 15, 20, 10]
bar_data2 = [8, 12, 25, 18]
bar_labels1 = ['A', 'B', 'C', 'D']
bar_labels2 = ['P', 'Q', 'R', 'S']

labels = ['Yes', 'No']
colors = ['#66c2a5', '#fc8d62']

# Adjustable radius
donut_radius = 1.3  # Change this value to adjust donut size

# Create the figure
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1], figure=fig)

# Top left section: Bar chart
ax_top_left = fig.add_subplot(gs[0, 0])
create_bar_chart(ax_top_left, bar_data1, bar_labels1, "Top Left Bar Chart")

# Top right section (for donut charts)
gs_right = gridspec.GridSpecFromSubplotSpec(
    2, 3, subplot_spec=gs[0, 1], wspace=0.25, hspace=0.25
)

# Add donut charts in triangular arrangement
ax_donut1 = fig.add_subplot(gs_right[0, 1])  # Top-center
ax_donut2 = fig.add_subplot(gs_right[1, 0])  # Bottom-left
ax_donut3 = fig.add_subplot(gs_right[1, 2])  # Bottom-right

# Create donut charts
create_donut(ax_donut1, data1, labels, colors, "Donut 1", donut_radius)
create_donut(ax_donut2, data2, labels, colors, "Donut 2", donut_radius)
create_donut(ax_donut3, data3, labels, colors, "Donut 3", donut_radius)

# Bottom section: Full-width bar chart
ax_bottom = fig.add_subplot(gs[1, :])
create_bar_chart(ax_bottom, bar_data2, bar_labels2, "Bottom Bar Chart")

# Adjust layout and display
plt.tight_layout()
plt.show()
