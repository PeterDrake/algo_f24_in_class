from digraph import *
from dfs import *

class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.marked = [False for _ in graph.adj]
        self.answer = []
        self.run()

    def run(self):
        # run dfs for each node, i.e. each sub list in adj
        for node in range(len(self.graph.adj)):
            self.dfs(node)
        # I don't know how to add things to the beginning of a list so I reverse the final product at the end
        self.answer = self.answer[::-1]

    def dfs(self, v):
        # if we've already visited, leave
        if self.marked[ v ]:
            return
        # now we've visited v
        self.marked[ v ] = True
        # check its unexplored children
        for w in self.graph.adj[v]:
            if not self.marked[ w ]:
                self.dfs(w)
        # add it to what will be the head, when we reverse
        self.answer.append(v)

    def find_index(self, v):
        for i in range(len(self.graph)):
            if self.graph.adj[i] == v:
                return i

g = Digraph(9)
g.add_edge(0, 1)
g.add_edge(0, 7)
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(2, 5)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(6, 7)

t = TopologicalSort(g)
print(t.answer)
