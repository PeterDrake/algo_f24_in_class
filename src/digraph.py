class Digraph:

    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def neighbors(self, v):
        return self.adj[v]


def transpose(g):
    result = Digraph(len(g.adj))
    for v in range(len(g.adj)):
        for w in g.neighbors(v):
            result.add_edge(w, v)
    return result
