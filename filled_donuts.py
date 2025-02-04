import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Create a full donut chart (single wedge covering 100%)
ax.pie([1], radius=1, colors=["black"], wedgeprops=dict(width=0.3, edgecolor="white"))

# Create a radial color gradient from red to green
r = np.linspace(0, 1, 100)  # Radial values
theta = np.linspace(0, 2 * np.pi, 100)  # Angular values
R, Theta = np.meshgrid(r, theta)  # Create meshgrid
X, Y = R * np.cos(Theta), R * np.sin(Theta)  # Convert to cartesian coordinates

# Define a colormap from red to green
cmap = mcolors.LinearSegmentedColormap.from_list("red_green", ["red", "yellow", "green"])
gradient = cmap(R)  # Apply colormap to radial gradient

# Plot the color-filled inner circle
ax.imshow(gradient, extent=[-0.7, 0.7, -0.7, 0.7], origin='lower', aspect='auto', zorder=2)

# Remove axis
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

plt.show()
