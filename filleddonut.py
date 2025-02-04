import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Example values for the donut (yes, no)
yes = 70  # Positive value
no = 30   # Negative value
total = yes + no  # Total value

# Normalize the total value to a range [0,1] for colormap
norm = mcolors.Normalize(vmin=0, vmax=100)  # Assuming total is between 0 and 100
cmap = mcolors.LinearSegmentedColormap.from_list("red_green", ["red", "yellow", "green"])
inner_color = cmap(norm(total))  # Get corresponding color

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Donut chart (yes vs. no)
sizes = [yes, no]
colors = ["green", "red"]
ax.pie(sizes, radius=1, colors=colors, wedgeprops=dict(width=0.3, edgecolor="white"))

# Add a solid-colored inner circle
circle = plt.Circle((0, 0), 0.5, color=inner_color, ec="black", lw=2)
ax.add_artist(circle)

# Display the total value at the center
ax.text(0, 0, f"{total}", ha='center', va='center', fontsize=18, fontweight='bold', color="black")

# Remove axis
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()
