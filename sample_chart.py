
from CustomSubplotGrid import CustomSubplotGrid
from stacked_bar_plotter import StackedBarPlotter
import pandas as pd

df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "X": [10, 20, 30],
    "Y": [15, 25, 35],
    "Z": [5, 10, 15]
})

subplots = [1,2,2]
ratios = [
    [2],         # Full-width
    [1, 1],
    [1, 1]# First 2x wider
    # [1, 1, 2, 1] # Third is 2x wider
]


grid = CustomSubplotGrid(subplots_per_row=subplots, ratios_per_row=ratios, figsize=(23,16))
fig, ax_grid = grid.create()
fig.suptitle('ABC',fontsize=30)
plotter = StackedBarPlotter(df, category_col="Category", value_cols=["X", "Y", "Z"])
plotter.plot(title="My Custom Stacked Bar", percentage=True, horizontal=False,ax=ax_grid[0][0])
