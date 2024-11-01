class Digraph:

    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].add(w)

    def neighbors(self, v):
        return self.adj[v]
