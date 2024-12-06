import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
G.add_nodes_from(names)

# Add edges (connections with directions)
edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Alice", "David"), ("David", "Bob"), ("Eve", "Charlie")]
G.add_edges_from(edges)

# Define positions for nodes
pos = nx.spring_layout(G)

# Create the plot
plt.figure(figsize=(8, 8))

# Draw nodes with boxes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_shape="s", node_color="lightblue", edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Draw edges with arrows in the middle
for edge in G.edges():
    start, end = edge
    # Compute the positions of the start and end nodes
    start_pos = pos[start]
    end_pos = pos[end]
    # Compute the midpoint
    midpoint = (start_pos + end_pos) / 2
    # Draw a straight line between the nodes
    plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color="gray", zorder=1, lw=1.5)
    # Add an arrow at the midpoint
    plt.annotate(
        "",
        xy=end_pos,
        xytext=midpoint,
        arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
    )

# Add plot title and show
plt.title("Directional Network Plot with Mid-Edge Arrows", fontsize=14)
plt.axis("off")
plt.show()
