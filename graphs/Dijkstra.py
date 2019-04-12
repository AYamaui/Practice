from graph import Graph

def initialize_costs(graph, start_vertex):
    costs = {}

    for vertex in graph.adjacency_list:
        costs[vertex] = float("inf")

    costs[start_vertex] = 0

    return costs


def extract_min(pending_edges):
    min_weight = float('inf')
    min_idx = None

    for idx, (v1, v2, weight) in enumerate(pending_edges):
        if weight < min_weight:
            min_weight = weight
            min_idx = idx

    return pending_edges.pop(min_idx)

def dijkstra(graph, vertex):
    costs = initialize_costs(graph, vertex)
    n_vertices = len(graph.adjacency_list.keys())
    pending_edges = []
    visited = [vertex]
    vertex_to_explore = vertex
    parent = {vertex: None}

    while len(visited) < n_vertices:

        for neighbor in graph.adjacency_list[vertex_to_explore]:
            if neighbor not in visited:
                pending_edges.append((vertex_to_explore, neighbor, graph.weights[(vertex_to_explore, neighbor)]))

        if not pending_edges:
            break

        v1, v2, weight = extract_min(pending_edges)

        if costs[v2] > costs[v1] + weight:
            costs[v2] = costs[v1] + weight
            parent[v2] = v1

        visited.append(vertex_to_explore)
        vertex_to_explore = v2

    return parent


if __name__ == '__main__':
    g = Graph()
    g.insert('g', 'y', 19)
    g.insert('g', 'p', 7)
    g.insert('y', 'r', 4)
    g.insert('y', 'p', 11)
    g.insert('p', 'r', 15)
    g.insert('p', 'b', 5)
    g.insert('r', 'b', 13)

    print(dijkstra(g, 'g'))
