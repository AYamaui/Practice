from graph import Graph


def DFS_visit(graph, vertex, parent):

    for neighbor in graph.adjacency_list[vertex]:
        if neighbor not in parent:
            parent[neighbor] = vertex
            DFS_visit(graph, neighbor, parent)

    return parent


def DFS(graph):
    parent = {}

    for vertex in graph.adjacency_list.keys():
        if vertex not in parent:
            parent[vertex] = None
            # print(DFS_visit(graph, vertex, parent))
            print(DFS_with_cycle_detection(graph, vertex, parent, []))

def find_tree_edges():
    pass

def find_forward_edges():
    pass

# Important for cycles detection
def find_backward_edges():
    pass

def find_cross_edges():
    pass


# G has a cycle <=> DFS has a backward edge
def DFS_with_cycle_detection(graph, vertex, parent, stack):

    for neighbor in graph.adjacency_list[vertex]:

        if neighbor in stack:
            cycle = stack[stack.index(neighbor):] + [neighbor]
            print('Cycle detected: {}'.format(cycle))
        if neighbor not in parent:
            stack.append(neighbor)
            parent[neighbor] = vertex
            DFS_with_cycle_detection(graph, neighbor, parent, stack)
            stack.pop()

    return parent

# runs DFS and output the reverse of finishing time of vertices
def topological_sort():
    pass


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

    print(DFS_visit(g, 's', {'s': None}))
    DFS(g)

    print('-------------------------------------')
    g2 = Graph(oriented=True)
    g2.insert('a', 'b')
    g2.insert('a', 'd')
    g2.insert('b', 'e')
    g2.insert('e', 'd')
    g2.insert('d', 'b')
    g2.insert('c', 'e')
    g2.insert('c', 'f')
    g2.insert('f', 'f')

    DFS(g2)

