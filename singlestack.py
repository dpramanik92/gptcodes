import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Example DataFrame
data = {
    "keys": ["A", "B", "C", "D", "E"],
    "values": [10, 20, 30, 40, 50],
}
df = pd.DataFrame(data)

# Specify the keys of the rows to sum
keys_to_sum = ["B", "D"]

# Filter the DataFrame to only include the specified keys
filtered_rows = df[df["keys"].isin(keys_to_sum)]

# Calculate the sum of the "values" column for these rows
sum_of_values = filtered_rows["values"].sum()

# Add the new row to the DataFrame
new_row = {"keys": "+".join(keys_to_sum), "values": sum_of_values}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Plot the stacked bar chart
fig, ax = plt.subplots(figsize=(6, 4))

# Data for the bar chart
keys = df["keys"]
values = df["values"]
total_sum = values.sum()  # Total sum for percentage calculation
bottom = 0
bar_width = 0.5  # Set the bar width

# Create a single stacked bar
for i, (key, value) in enumerate(zip(keys, values)):
    ax.bar(0, value, width=bar_width, bottom=bottom, label=f"{key} ({value})", color=f"C{i}")
    
    # Annotate with percentage
    percentage = (value / total_sum) * 100
    mid_point = bottom + value / 2  # Midpoint of the segment for annotation
    ax.text(0, mid_point, f"{percentage:.1f}%", ha='center', va='center', color="white", fontsize=10, fontweight='bold')
    
    bottom += value  # Update the bottom for stacking

# Customize the plot
ax.set_xticks([0])
ax.set_xticklabels(["Category"])
ax.set_ylabel("Values")
ax.set_title("Stacked Bar Chart with Percentage Annotations")

# Move the legend outside the bar
ax.legend(title="Keys", loc="upper right", frameon=False)

# Adjust the x-axis limits for better visualization
ax.set_xlim(-0.5, 0.5)

# Show the plot
plt.tight_layout()
plt.show()
