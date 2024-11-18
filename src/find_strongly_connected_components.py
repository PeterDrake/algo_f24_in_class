from digraph import Digraph, transpose

def find_strongly_connected_components(graph: Digraph) -> list[int]:
    """
    O(E)
    """

    finishing_order = []
    explored = [False for _ in range(len(graph.adj))]

    def DFS_first(node: int):
        if explored[node]:
            return
        explored[node] = True
        for neigh in graph.neighbors(node):
            DFS_first(neigh)

        # Don't add this node to the ordering unless all its children
        # are already in the list after.
        finishing_order.append(node)


    for node in range(len(graph.adj)):
        DFS_first(node)

    graph_T = transpose(graph)

    components = [-1 for _ in range(len(graph.adj))]

    def DFS_second(node: int, root: int):
        if components[node] != -1:
            return
        components[node] = root
        for child in graph_T.neighbors(node):
            DFS_second(child, root)

    for node in finishing_order[::-1]:
        DFS_second(node, node)

    return components

if __name__ == "__main__":
    graph = Digraph(8)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(1, 5)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(3, 2)
    graph.add_edge(3, 7)
    graph.add_edge(4, 0)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)
    graph.add_edge(6, 7)
    graph.add_edge(7, 7)
    for i in range(len(graph.adj)):
        print(i, graph.adj[i])
    components = find_strongly_connected_components(graph)
    print(components)
