

class Graph:

    def __init__(self, oriented=False):
        self.adjacency_list = {}
        self.oriented = oriented
        self.weights = {}

    def __str__(self):

        for vertex, adjacents in self.adjacency_list.items():
            for neighbor in adjacents:
                print('{} - {}'.format(vertex, neighbor))

    def insert(self, v1, v2, weight=None):
        self.adjacency_list.setdefault(v1, [])
        self.adjacency_list[v1].append(v2)

        if weight:
            self.weights[(v1, v2)] = weight

        if not self.oriented:
            self.adjacency_list.setdefault(v2, [])
            self.adjacency_list[v2].append(v1)
            self.weights[(v2, v1)] = weight


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

    print(g)

