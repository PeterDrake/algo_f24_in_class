from digraph import *

class Traverse:

    def __init__(self, graph):
        self.marked = [False for _ in graph.adj]
        self.result = []
        self.traverse(graph)
        print(f"{self.result}")

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj[v]:
            if not self.marked[w]:
                self.dfs(graph, w)
        self.result.append(v)

    def traverse(self, graph):
        for vertex in range(len(graph.adj)):
            if not self.marked[vertex]:
                self.dfs(graph, vertex)
        self.result = self.result[::-1]


g = Digraph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(0, 7)
g.add_edge(6, 7)
g.add_edge(1, 7)

Traverse(g)