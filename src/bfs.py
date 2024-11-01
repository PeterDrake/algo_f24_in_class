from collections import deque


class BreadthFirst:

    def __init__(self, graph, start):
        self.marked = [False for _ in graph.adj]
        self.distance = [float('inf') for _ in graph.adj]
        self.edge = [None for _ in graph.adj]
        self.bfs(graph, start)

    def bfs(self, graph, start):
        q = deque()
        self.distance[start] = 0
        self.marked[start] = True
        q.append(start)
        while len(q):
            v = q.popleft()
            for w in graph.adj[v]:
                if not self.marked[w]:
                    self.edge[w] = v
                    self.distance[w] = self.distance[v] + 1
                    self.marked[w] = True
                    q.append(w)

    def path_to(self, v):
        if not self.marked[v]:
            return None
        path = []
        x = v
        while self.distance[x] != 0:
            path.append(x)
            x = self.edge[x]
        path.append(x)
        return path[::-1]
