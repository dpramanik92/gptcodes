import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories_top = ["A", "B", "C", "D", "E"]
values_top = [10, 20, 15, 25, 18]

categories_bottom = ["P", "Q", "R", "S"]
values_bottom = [
    [5, 15, 10, 20],
    [8, 18, 12, 22],
    [6, 16, 9, 19],
    [7, 17, 11, 21]
]

titles = ["Chart 1", "Chart 2", "Chart 3", "Chart 4"]
colors = ["seagreen", "darkorange", "purple", "crimson"]

# Create a figure with subplots (2 rows: 1 large chart on top, 4 smaller charts in bottom row)
fig, ax = plt.subplots(2, 4, figsize=(16, 8), gridspec_kw={'height_ratios': [2, 1]})

# ---- Top Half: Large Horizontal Bar Chart ----
ax[0, 0].barh(categories_top, values_top, color="royalblue")
ax[0, 0].set_title("Top Half: Large Horizontal Bar Chart")
ax[0, 0].invert_yaxis()  # Keep highest value at the top
ax[0, 0].grid(axis='x', linestyle='--', alpha=0.7)

# Hide the extra empty plots in the top row
for i in range(1, 4):
    ax[0, i].axis("off")

# ---- Bottom Half: Four Smaller Horizontal Bar Charts (In a Single Row) ----
for i in range(4):  
    ax[1, i].barh(categories_bottom, values_bottom[i], color=colors[i])
    ax[1, i].set_title(titles[i])
    ax[1, i].invert_yaxis()  # Keep highest value at the top
    ax[1, i].grid(axis='x', linestyle='--', alpha=0.7)

# ---- Adjust Layout ----
plt.subplots_adjust(hspace=0.3, wspace=0.4)  # Adjust spacing

# Show the plot
plt.show()
