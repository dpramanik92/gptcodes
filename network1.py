import pandas as pd
import matplotlib.pyplot as plt

def plot_network_on_plane(
    df,
    name_col,
    manager_col,
    x_col,
    y_col,
    fig=None,
    ax=None,
    figsize=(10, 6),
    marker_color='steelblue',
    marker_size=8,
    arrow_color='gray',
    label_offset=0.5,
    title='Hierarchical Network in 2D Plane'
):
    """
    Plots a hierarchical network in a 2D plane using specified x/y coordinates.
    Arrows represent manager-subordinate relationships. Supports external fig, ax.

    Parameters:
    - df: pandas DataFrame
    - name_col: str, column with individual names
    - manager_col: str, column with manager names
    - x_col: str, column for x-coordinate (e.g., age)
    - y_col: str, column for y-coordinate (e.g., height)
    - fig: matplotlib Figure object (optional)
    - ax: matplotlib Axes object (optional)
    - figsize: tuple, size of figure if fig/ax not provided
    - marker_color: str, color of node markers
    - marker_size: int, marker size
    - arrow_color: str, color of arrows
    - label_offset: float, text offset from point
    - title: str, plot title
    """

    # Create fig and ax if not provided
    if ax is None or fig is None:
        fig, ax = plt.subplots(figsize=figsize)

    # Clean data
    df_clean = df.dropna(subset=[name_col, x_col, y_col])

    # Create (x, y) positions for each individual
    pos = {
        row[name_col]: (row[x_col], row[y_col])
        for _, row in df_clean.iterrows()
    }

    # Plot each node and label
    for name, (x, y) in pos.items():
        ax.plot(x, y, 'o', color=marker_color, markersize=marker_size)
        ax.text(x + label_offset, y + label_offset, str(name), fontsize=9)

    # Draw arrows from manager to subordinate
    for _, row in df_clean.iterrows():
        manager = row.get(manager_col)
        employee = row[name_col]
        if pd.notna(manager) and manager in pos and employee in pos:
            x0, y0 = pos[manager]
            x1, y1 = pos[employee]
            ax.annotate(
                '', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1)
            )

    # Final touches
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    ax.grid(True)

    return fig, ax
