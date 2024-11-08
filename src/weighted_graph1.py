class WeightedGraph:

    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w, weight):
        self.adj[v].append((w, weight))
        self.adj[w].append((v, weight))

    def neighbors(self, v):
        return self.adj[v]