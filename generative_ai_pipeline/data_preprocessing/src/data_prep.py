import matplotlib.pyplot as plt
import networkx as nx

# Define the flow diagram structure
g = nx.DiGraph()

# Add nodes
g.add_nodes_from(
    [
        "Data Collection",
        "Data Preprocessing",
        "Customer Segmentation",
        "Behavioral Analysis",
        "LLM Integration",
        "Predictive Analytics",
        "Visualization",
        "Monitoring",
    ]
)

# Add edges
g.add_edges_from(
    [
        ("Data Collection", "Data Preprocessing"),
        ("Data Preprocessing", "Customer Segmentation"),
        ("Customer Segmentation", "Behavioral Analysis"),
        ("Behavioral Analysis", "LLM Integration"),
        ("Behavioral Analysis", "Predictive Analytics"),
        ("LLM Integration", "Visualization"),
        ("Predictive Analytics", "Visualization"),
        ("Visualization", "Monitoring"),
    ]
)

# Define node positions
pos = {
    "Data Collection": (0, 3),
    "Data Preprocessing": (1, 3),
    "Customer Segmentation": (2, 3),
    "Behavioral Analysis": (3, 3),
    "LLM Integration": (3, 2),
    "Predictive Analytics": (4, 3),
    "Visualization": (5, 2.5),
    "Monitoring": (6, 2.5),
}

# Draw the graph
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(g, pos, node_color="skyblue", node_size=2000)
nx.draw_networkx_labels(g, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(
    g, pos, arrows=True, arrowstyle="->", connectionstyle="arc3,rad=0.1"
)

plt.title("High-Level Workflow for 9Mobile AI-Driven Solution", fontsize=14)
plt.axis("off")
plt.show()
