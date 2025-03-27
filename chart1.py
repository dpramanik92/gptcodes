import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.arange(1, 6)
y = np.array([10, 15, 7, 20, 18])

donut_data = [
    [30, 70],  # First donut (e.g., 30% Yes, 70% No)
    [50, 50],  # Second donut
    [20, 80]   # Third donut
]
labels = ["Yes", "No"]

# Creating the Figure
fig, ax = plt.subplots(2, 1, figsize=(8, 8), gridspec_kw={'height_ratios': [1, 2]})

# ---- Top Half: Line Plot with Markers ----
ax[0].plot(x, y, marker='o', linestyle='-', color='b', label="Trend")
ax[0].set_xticks(x)
ax[0].set_ylabel("Value")
ax[0].set_title("Line Plot with Markers")
ax[0].legend()
ax[0].grid(True)

# ---- Bottom Half: Three Donut Charts ----
donut_colors = [["#ff9999", "#66b3ff"], ["#99ff99", "#ffcc99"], ["#c2c2f0", "#ffb3e6"]]
total_values = [sum(d) for d in donut_data]

# Creating three subplots for donuts
for i in range(3):
    ax_donut = fig.add_subplot(2, 3, i + 4)  # Subplot grid: 2 rows, 3 columns, position i+4
    wedges, texts, autotexts = ax_donut.pie(
        donut_data[i], labels=labels, autopct='%1.0f%%', colors=donut_colors[i],
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'}, startangle=90, pctdistance=0.85
    )
    
    # Draw a white circle at the center to make it a donut
    centre_circle = plt.Circle((0, 0), 0.6, color='white', fc='white')
    ax_donut.add_artist(centre_circle)
    
    # Add total at the center
    ax_donut.text(0, 0, str(total_values[i]), fontsize=12, fontweight="bold", ha='center', va='center')

    ax_donut.set_title(f"Donut {i+1}")

# Adjust Layout
plt.tight_layout()
plt.show()
