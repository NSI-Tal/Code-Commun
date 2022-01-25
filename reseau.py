import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
l = ["A", "B", "C", "D", "E", "F", "G", "H"]
for a in l:
    g.add_node(a)

g.add_edge("B", "D")
g.add_edge("B", "A")
g.add_edge("C", "A")
g.add_edge("C", "E")
g.add_edge("C", "H")
g.add_edge("G", "H")
g.add_edge("E", "A")
g.add_edge("E", "D")
g.add_edge("E", "F")

nx.draw(g, with_labels=True, font_weight='bold',
node_size=800, node_color='lightgrey')
plt.show()