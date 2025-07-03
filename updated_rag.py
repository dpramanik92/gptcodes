import pandas as pd
import matplotlib.pyplot as plt

def plot_z_points_from_wide(df_wide, name_col='name', threshold=20):
    # Extract all month columns (excluding the name column)
    month_cols = [col for col in df_wide.columns if col != name_col]

    # Melt the wide DataFrame to long format
    df_long = df_wide.melt(id_vars=name_col, 
                           value_vars=month_cols,
                           var_name='month',
                           value_name='z')

    # Define month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_long['month'] = pd.Categorical(df_long['month'], categories=month_order, ordered=True)
    df_long = df_long.sort_values([name_col, 'month'])

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    names = df_long[name_col].unique()
    name_to_y = {name: i for i, name in enumerate(names)}

    for _, row in df_long.iterrows():
        x = row['month']
        y = name_to_y[row[name_col]]
        color = 'red' if row['z'] < threshold else 'black'
        ax.plot(x, y, 'o', color=color)

    ax.set_yticks(list(name_to_y.values()))
    ax.set_yticklabels(list(name_to_y.keys()))
    ax.set_xticks(month_order)
    ax.set_xlabel("Month")
    ax.set_ylabel("Name")
    ax.set_title(f"Points with Red if z < {threshold}")
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
