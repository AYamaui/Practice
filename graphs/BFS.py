from graph import Graph


def BFS(graph, start_vertex):
    visited = {start_vertex: 0}
    frontier = [start_vertex]
    level_idx = 1

    while frontier:
        next = []
        for vertex in frontier:
            for neighbor in graph.adjacency_list[vertex]:

                if neighbor not in visited:
                    visited[neighbor] = level_idx
                    next.append(neighbor)
        frontier = next
        level_idx += 1

    return visited


if __name__ == '__main__':
    g = Graph()
    g.insert('s', 'a')
    g.insert('s', 'x')
    g.insert('a', 'z')
    g.insert('x', 'c')
    g.insert('x', 'd')
    g.insert('c', 'd')
    g.insert('c', 'f')
    g.insert('c', 'v')
    g.insert('d', 'f')
    g.insert('f', 'v')

    print(BFS(g, 's'))


