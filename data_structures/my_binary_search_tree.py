
class Node:

    def __init__(self, value, parent):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = parent

    def __str__(self):
        print(self.value)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def recursive_print(node, type):

        if node:

            if type == 'R':
                print('R: {}'.format(node.value))
            elif type == 'L':
                print('L: {}'.format(node.value))
            else:
                print(node.value)

            BinarySearchTree.recursive_print(node.left_child, 'L')
            BinarySearchTree.recursive_print(node.right_child, 'R')
        return

    def __str__(self):

        BinarySearchTree.recursive_print(self.root)

    def insert(self, element, node):

        if not self.root:
            self.root = Node(element, None)
            return

        if node.value <= element:

            if node.right_child:
                self.insert(element, node.right_child)
            else:
                node.right_child = Node(element, node)
        else:

            if node.left_child:
                self.insert(element, node.left_child)
            else:
                node.left_child = Node(element, node)

    def remove(self, element):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    # next larger
    def find_successor(self):
        pass

    # next smaller
    def find_predecessor(self):
        pass


if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(10, None)
    bst.insert(8, bst.root)
    bst.insert(11, bst.root)
    bst.insert(1, bst.root)
    bst.insert(3, bst.root)
    bst.insert(15, bst.root)
    bst.insert(28, bst.root)

    BinarySearchTree.recursive_print(bst.root, None)


