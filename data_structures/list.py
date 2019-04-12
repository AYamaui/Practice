

class List:

    def __init__(self):
        self.size = 0
        self.elements = {}

    def __repr__(self):
        return '<List size: {} elements: {}>'.format(self.size, self.elements.values())

    def __str__(self):
        return str([elem[1] for elem in sorted(self.elements.items())])

    # Complexity: O(1)
    def is_empty(self):
        return self.size == 0

    # Complexity: O(1)
    def get_elem(self, idx):

        try:
            return self.elements[idx]
        except KeyError:
            raise KeyError('The index is invalid!')

    # Complexity: O(1)
    def append(self, element):
        self.elements[self.size] = element
        self.size += 1

    # Complexity: O(n)
    def prepend(self, element):

        for i in range(self.size - 1, -1, -1):
            self.elements[i + 1] = self.elements[i]

        self.elements[0] = element

        self.size += 1

    # Complexity: O(n)
    def insert(self, index, element):

        if index > self.size or index < 0:
            raise IndexError('Invalid index!')

        for i in range(self.size - 1, index - 1, -1):
            self.elements[i + 1] = self.elements[i]

        self.elements[index] = element

        self.size += 1

    # Complexity: O(1)
    def pop(self):

        if self.is_empty():
            raise Exception('Empty array')

        elem = self.elements[self.size - 1]
        del self.elements[self.size - 1]

        self.size -= 1

        return elem

    # Complexity: O(n)
    def remove(self, element):

        if self.size == 0:
            raise Exception('Empty array')

        last_occupied_idx = -1

        idxs = self.find(element)

        for i in range(self.size):

            if i not in idxs:
                self.elements[last_occupied_idx + 1] = self.elements[i]
                last_occupied_idx += 1

        positions_to_remove = self.size - len(idxs) - 1

        for i in range(self.size - 1, positions_to_remove, -1):
            del self.elements[i]

        self.size -= len(idxs)

    # Complexity: O(n)
    def find(self, element):
        idxs = [idx for idx, elem in self.elements.items() if elem == element]

        return idxs


if __name__ == '__main__':
    array = List()
    array.append(3)
    array.append(22)
    array.append(143)
    array.append(2)
    array.append(90)
    array.append(11)
    array.append(8)
    array.append(2)

    print(array)

    print('Empty: {}'.format(array.is_empty()))
    print('3th elem: {}'.format(array.get_elem(2)))

    array.prepend(144)
    print(array)
    print(array.elements)
    array.insert(4, 89)
    print(array)
    print(array.elements)
    print('Pop: {}'.format(array.pop()))
    print(array)
    print('Append 2')
    array.append(2)
    print(array)
    print('Remove 2')
    array.remove(2)
    print(array)
    print(array.elements)


