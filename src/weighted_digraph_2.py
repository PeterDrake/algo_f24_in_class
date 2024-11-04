class WeightedDigraph:

    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w, weight):
        self.adj[v].append((w, weight))

    def neighbors(self, v):
        return self.adj[v]