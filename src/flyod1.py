from weighted_graph1 import WeightedGraph
from math import inf

def ShortestPaths(graph):
    num_vert = len(graph.adj)

    distance = [[inf for _ in range(num_vert)] for _ in range (num_vert)]

    # set diagnoal to zero
    for i in range(num_vert):
        distance[i][i] = 0

    for v in range(num_vert):
        for w, weight in graph.adj[v]:
            distance[v][w] = weight

    for k in range(num_vert):
        for i in range(num_vert):
            for j in range(num_vert):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance



graph = WeightedGraph(7)
graph.add_edge(0,1, 6)
graph.add_edge(1,2,4)
graph.add_edge(0,3,1)
graph.add_edge(2,4,1)
graph.add_edge(0,2,5)
graph.add_edge(3,4,1)
graph.add_edge(5,6,2)


d= ShortestPaths(graph)
for row in d:
    print(row)







