import matplotlib.pyplot as plt
import numpy as np

# Define the dimensions of the gradient
width, height = 500, 500
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)

# Calculate the radial distance from the top-right corner
distance_from_top_right = np.sqrt((X - 1)**2 + (Y - 1)**2)

# Normalize the distance to range from 0 to 1
gradient = distance_from_top_right / distance_from_top_right.max()

# Plot the radial gradient
plt.figure(figsize=(6, 6))
plt.imshow(gradient, extent=[0, 1, 0, 1], origin='lower', cmap='viridis')
plt.title("Radial Gradient Fixed at Top Right")
plt.colorbar(label='Gradient Intensity')
plt.show()
