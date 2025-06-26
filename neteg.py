# Sample data
df = pd.DataFrame({
    'Person': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Manager': [None, 'Alice', 'Alice', 'Bob', 'Charlie'],
    'Age': [45, 38, 33, 29, 25],
    'Height': [165, 170, 168, 175, 160]
})

# Call function with custom column names
fig, ax = plot_network_on_plane(
    df,
    name_col='Person',
    manager_col='Manager',
    x_col='Age',
    y_col='Height',
    title='Company Hierarchy on Age-Height Plot'
)

plt.tight_layout()
plt.show()
