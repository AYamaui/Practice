

class MaxHeap:

    def __init__(self, array):
        self.array = [-1] + array
        self.height = len(array)

        self.build_max_heap(self.array)

    def build_max_heap(self, array):

        for i in range(len(array)//2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, node_idx):
        children = []
        left_child = 2 * node_idx
        right_child = 2 * node_idx + 1

        if self.height >= left_child:
            children.append((left_child, self.array[left_child]))
        if self.height >= right_child:
            children.append((right_child, self.array[right_child]))

        if children:
            max_child = max(children, key=lambda x: x[1])

            if max_child[1] > self.array[node_idx]:
                aux = self.array[node_idx]
                self.array[node_idx] = max_child[1]
                self.array[max_child[0]] = aux

            if self.height >= left_child:
                self.max_heapify(left_child)
            if self.height >= right_child:
                self.max_heapify(right_child)

        return

    def insert(self, value):
        pass

    def max(self):
        pass

    def extract_max(self):
        pass

    def increase_key(self, value, new_index):
        pass


if __name__ == '__main__':
    array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    max_heap = MaxHeap(array)
    print(max_heap.array)
