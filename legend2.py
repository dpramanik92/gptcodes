import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y_values = [np.sin(x), np.cos(x), np.sin(2*x), np.cos(2*x), np.sin(3*x), np.cos(3*x), 
            np.sin(4*x), np.cos(4*x)]

# Labels (2 in one group, 6 in another)
labels_group_1 = ["Group A1", "Group A2"]
labels_group_2 = ["Group B1", "Group B2", "Group B3", "Group B4", "Group B5", "Group B6"]

# Colors and styles for differentiation
styles = ['-', '--', '-.', ':', '-', '--', '-.', ':']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

fig, ax = plt.subplots()

# Plotting
for i, (y, style, color) in enumerate(zip(y_values, styles, colors)):
    label = labels_group_1[i] if i < 2 else labels_group_2[i - 2]
    ax.plot(x, y, linestyle=style, color=color, label=label)

# Creating the legend with a custom layout
handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1), ncol=2, 
                   title="Legend", columnspacing=1.5, labelspacing=0.8)

# Show the plot
plt.show()
