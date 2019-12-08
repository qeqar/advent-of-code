#!/usr/bin/env python
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

with open('inputs/day06.txt') as f:
    orbits = f.readlines()

#orbits = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
#orbits = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]

for edge in orbits:
    e1, e2 = edge.split(")")
    e2 = e2.strip()
    graph.add_nodes_from([e1, e2])
    graph.add_edge(e1, e2)

print(graph.edges)


print(networkx.shortest_path_length(graph, "YOU", "SAN") - 2)
total_orbits = 0
for node in graph.nodes:
    total_orbits += networkx.shortest_path_length(graph, node, "COM")



print("total orbits: " + str(total_orbits))
networkx.draw(graph)
plt.show()
