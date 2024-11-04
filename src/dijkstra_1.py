import heapq

class Dijkstra:
    def __init__(self, graph, start):
        self.distance = [float('inf') for _ in graph.adj]
        self.edge = [None for _ in graph.adj]
        self.search(graph, start)

    def search(self, graph, start):
        self.distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            _,node = heapq.heappop(q)

            # relax
            for neighbor, weight in graph.adj[node]:
                if self.distance[node] + weight < self.distance[neighbor]:
                    self.distance[neighbor] = self.distance[node] + weight
                    self.edge[neighbor] = node
                    heapq.heappush(q, (self.distance[neighbor], neighbor))


    def path_to(self, v):
        if self.distance[v] == float("inf"):
            return None
        path = []
        x = v
        while self.distance[x] != 0:
            path.append(x)
            x = self.edge[x]
        path.append(x)
        return path[::-1]


from weighted_digraph_1 import WeightedDigraph

g = WeightedDigraph(5)
g.add_edge(0, 1, 4)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 6)
g.add_edge(0, 2, 2)
g.add_edge(2, 1, 1)

d = Dijkstra(g, 0)
print(d.path_to(4))