import pandas as pd
import matplotlib.pyplot as plt

# Example data
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'manager': [None, 'Alice', 'Alice', 'Bob', 'Charlie'],
    'age': [45, 38, 33, 29, 25],
    'height': [165, 170, 168, 175, 160]
})

# Create a mapping from name to (age, height)
pos = {row['name']: (row['age'], row['height']) for _, row in df.iterrows()}

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot for all nodes
for name, (age, height) in pos.items():
    plt.plot(age, height, 'o', markersize=8, color='steelblue')  # simple marker
    plt.text(age + 0.5, height + 0.5, name, fontsize=9)

# Draw arrows from manager to employee
for _, row in df.iterrows():
    if pd.notna(row['manager']):
        x_start, y_start = pos[row['manager']]
        x_end, y_end = pos[row['name']]
        plt.annotate(
            '', xy=(x_end, y_end), xytext=(x_start, y_start),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1)
        )

plt.xlabel("Age")
plt.ylabel("Height")
plt.title("Hierarchy Network in Age-Height Plane")
plt.grid(True)
plt.tight_layout()
plt.show()
