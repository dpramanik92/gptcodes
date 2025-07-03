import pandas as pd
import matplotlib.pyplot as plt

def plot_z_points(df, name_col='name', month_col='month', z_col='z', threshold=20):
    # Ensure consistent month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
    df = df.sort_values([name_col, month_col])

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Convert names to Y positions
    names = df[name_col].unique()
    name_to_y = {name: i for i, name in enumerate(names)}
    
    # Plot each point
    for _, row in df.iterrows():
        x = row[month_col]
        y = name_to_y[row[name_col]]
        color = 'red' if row[z_col] < threshold else 'black'
        ax.plot(x, y, 'o', color=color)

    # Set ticks and labels
    ax.set_yticks(list(name_to_y.values()))
    ax.set_yticklabels(list(name_to_y.keys()))
    ax.set_xticks(month_order)
    ax.set_xlabel("Month")
    ax.set_ylabel("Name")
    ax.set_title(f"Points with Red if {z_col} < {threshold}")
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
