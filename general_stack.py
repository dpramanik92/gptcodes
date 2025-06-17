import matplotlib.pyplot as plt

def plot_stacked_bar_with_annotations(
    df, category_col, value_cols,
    ax=None, colors=None, title="Stacked Bar Chart",
    percentage=False, horizontal=False
):
    """
    Plots a vertical or horizontal stacked bar chart with annotations.

    Parameters:
    - df: DataFrame
    - category_col: str, x-axis categories
    - value_cols: list of str, stacked column names
    - ax: matplotlib Axes (optional)
    - colors: list of color hex or tuple (optional)
    - title: str, chart title
    - percentage: bool, if True normalize stacks to 100%
    - horizontal: bool, if True plot horizontal bars
    """
    import numpy as np

    created_ax = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        created_ax = True

    categories = df[category_col]
    x = range(len(categories))
    data = df[value_cols].copy()

    if percentage:
        data = data.div(data.sum(axis=1), axis=0).fillna(0) * 100

    if colors is None:
        colors = plt.cm.tab10.colors[:len(value_cols)]

    bottom = np.zeros(len(df))

    for i, col in enumerate(value_cols):
        values = data[col]
        color = colors[i % len(colors)]

        if horizontal:
            bars = ax.barh(x, values, left=bottom, label=col, color=color)
        else:
            bars = ax.bar(x, values, bottom=bottom, label=col, color=color)

        for j, val in enumerate(values):
            if val == 0:
                continue
            if horizontal:
                xpos = bottom[j] + val / 2
                ax.text(xpos, j, f"{val:.0f}%" if percentage else f"{val:.0f}",
                        va='center', ha='center', color='white', fontsize=9)
            else:
                ypos = bottom[j] + val / 2
                ax.text(j, ypos, f"{val:.0f}%" if percentage else f"{val:.0f}",
                        ha='center', va='center', color='white', fontsize=9)

        bottom += values

    if horizontal:
        ax.set_yticks(list(x))
        ax.set_yticklabels(categories)
        ax.set_xlabel("Percentage" if percentage else "Values")
    else:
        ax.set_xticks(list(x))
        ax.set_xticklabels(categories)
        ax.set_ylabel("Percentage" if percentage else "Values")

    ax.set_title(title)
    ax.legend(title="Components")

    if created_ax:
        plt.tight_layout()
        plt.show()

    return ax
