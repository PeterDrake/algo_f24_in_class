from Weighted_graph2 import *
def shortestpaths (graph):
    v= len(graph.adj)
    dist = [[float("inf") for _ in range(v)] for _ in range(v)]
    for i  in range (v):
        dist [i][i]= 0
        for j,weight in graph.adj[i]:
            dist[i][j]= weight
    for k in range (v):
        for w in range (v):
            for x in range(v):
                if dist[k][w] + dist[k][x] < dist[w][x]:
                    dist[w][x]= dist[k][w] + dist[k][x]
    return dist
g = WeightedGraph(7)
g.add_edge(0,1,4)
g.add_edge(0,2,5)
g.add_edge(1,2,6)
g.add_edge(2,3,1)
g.add_edge(3,4,1)
g.add_edge(0,4,1)
g.add_edge(5,6,2)
d=shortestpaths(g)

for row in d:
    print (row)

