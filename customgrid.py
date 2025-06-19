import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

class CustomSubplotGrid:
    def __init__(self, subplots_per_row, ratios_per_row=None, figsize=(12, 6), hspace=0.4, wspace=0.4):
        """
        Create a flexible subplot grid layout with full support for custom width ratios.

        Parameters:
        - subplots_per_row: list[int], number of subplots per row (e.g. [1, 2, 4])
        - ratios_per_row: list[list[float] or None], custom width ratios per row
        - figsize: tuple, figure size
        - hspace: float, vertical space between rows
        - wspace: float, horizontal space between columns
        """
        self.subplots_per_row = subplots_per_row
        self.ratios_per_row = ratios_per_row or [None] * len(subplots_per_row)
        self.figsize = figsize
        self.hspace = hspace
        self.wspace = wspace

        if len(self.subplots_per_row) != len(self.ratios_per_row):
            raise ValueError("ratios_per_row must match length of subplots_per_row.")

        self.fig = None
        self.ax_grid = []

    def create(self):
        nrows = len(self.subplots_per_row)
        max_cols = max([sum(r) if r else n for n, r in zip(self.subplots_per_row, self.ratios_per_row)])

        self.fig = plt.figure(figsize=self.figsize)
        self.ax_grid = []

        for row_idx, (ncols, ratios) in enumerate(zip(self.subplots_per_row, self.ratios_per_row)):
            if ratios:
                if len(ratios) != ncols:
                    raise ValueError(f"Row {row_idx+1}: ratios length must match number of subplots.")
                total_units = sum(ratios)
            else:
                ratios = [1] * ncols
                total_units = ncols

            # Create GridSpec with sufficient width
            gs = GridSpec(nrows, max_cols, figure=self.fig, hspace=self.hspace, wspace=self.wspace)
            row_axes = []

            start = (max_cols - total_units) // 2  # center-align
            for span in ratios:
                ax = self.fig.add_subplot(gs[row_idx, start:start + span])
                row_axes.append(ax)
                start += span

            self.ax_grid.append(row_axes)

        return self.fig, self.ax_grid



from custom_subplot_grid import CustomSubplotGrid
import matplotlib.pyplot as plt

subplots = [1, 2, 4]
ratios = [
    [1],         # Full-width
    [2, 1],      # First 2x wider
    [1, 1, 2, 1] # Third is 2x wider
]

grid = CustomSubplotGrid(subplots_per_row=subplots, ratios_per_row=ratios, figsize=(14, 8))
fig, ax_grid = grid.create()

# Plot something
for i, row in enumerate(ax_grid):
    for j, ax in enumerate(row):
        ax.plot([0, 1], [i, j])
        ax.set_title(f"Row {i+1} Col {j+1}")

plt.show()
