
class Node:

    def __init__(self, value, parent):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 0

    def __str__(self):
        print(self.value)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def recursive_print(node, type):

        if node:

            if type == 'R':
                print('R: {} -> {}, {}'.format(node.parent.value, node.value, node.height))
            elif type == 'L':
                print('L: {} -> {}, {}'.format(node.parent.value, node.value, node.height))
            else:
                print(node.value, node.height)

            BinarySearchTree.recursive_print(node.left_child, 'L')
            BinarySearchTree.recursive_print(node.right_child, 'R')
        return

    def __str__(self):

        BinarySearchTree.recursive_print(self.root, None)

    # def calculate_height(self, node):
    #
    #     if node.right_child:
    #         self.calculate_height(node.right_child)
    #         right_height = node.right_child.height
    #     else:
    #         right_height = -1
    #
    #     if node.left_child:
    #         self.calculate_height(node.left_child)
    #         left_height = node.left_child.height
    #     else:
    #         left_height = -1
    #
    #     node.height = 1 + max(left_height, right_height)

    def insert(self, element, node):

        if not self.root:
            self.root = Node(element, None)
            return

        if node.value <= element:

            if node.right_child:
                self.insert(element, node.right_child)
            else:
                node.right_child = Node(element, node)
                self.update_height(node)
                self.fix_AVL_property(node.right_child)
        else:

            if node.left_child:
                self.insert(element, node.left_child)
            else:
                node.left_child = Node(element, node)
                self.update_height(node)
                self.fix_AVL_property(node.left_child)

    def height(self, node):
        right_child_height = node.right_child.height if node.right_child else -1
        left_child_height = node.left_child.height if node.left_child else -1
        return max(left_child_height, right_child_height) + 1

    def update_height(self, node):

        if not node:
            return

        node.height = self.height(node)
        self.update_height(node.parent)

    def right_flatenning_rotation(self, grand_parent, parent, node):
        grand_parent.right_child = node
        node.parent = grand_parent
        parent.left_child = node.right_child
        node.right_child = parent
        parent.parent = node
        parent.height -= 1
        node.height += 1

    def left_flatenning_rotation(self, grand_parent, parent, node):
        grand_parent.left_child = node
        node.parent = grand_parent
        parent.right_child = node.left_child
        node.left_child = parent
        parent.parent = node
        parent.height -= 1
        node.height += 1

    def right_balancing_rotation(self, grand_parent, parent):
        grand_parent.left_child = parent.right_child

        if grand_parent.left_child:
            grand_parent.left_child.parent = grand_parent

        parent.parent = grand_parent.parent

        if grand_parent.parent.left_child == grand_parent:
            grand_parent.parent.left_child = parent
        else:
            grand_parent.parent.right_child = parent

        parent.right_child = grand_parent
        grand_parent.parent = parent

        if grand_parent.parent is None:
            self.root = grand_parent

        grand_parent.height = self.height(grand_parent)
        self.update_height(parent)

    def left_balancing_rotation(self, grand_parent, parent):
        grand_parent.right_child = parent.left_child

        if grand_parent.right_child:
            grand_parent.right_child.parent = grand_parent

        parent.parent = grand_parent.parent

        if grand_parent.parent.left_child == grand_parent:
            grand_parent.parent.left_child = parent
        else:
            grand_parent.parent.right_child = parent

        parent.left_child = grand_parent
        grand_parent.parent = parent

        if grand_parent.parent is None:
            self.root = grand_parent

        grand_parent.height = self.height(grand_parent)
        self.update_height(parent)

    def rotate(self, grand_parent, parent, node):

        if parent.left_child == node and grand_parent.left_child == parent:
            self.right_balancing_rotation(grand_parent, parent)
        elif parent.right_child == node and grand_parent.right_child == parent:
            self.left_balancing_rotation(grand_parentt, parent)
        elif grand_parent.right_child == parent:
            self.right_flatenning_rotation(grand_parent, parent, node)
            self.rotate(grand_parent, node, parent)
        else:
            self.left_flatenning_rotation(grand_parent, parent, node)
            self.rotate(grand_parent, node, parent)

    def fix_AVL_property(self, node, path=[]):
        path = [node] + path

        if not node:
            return

        left_child = node.left_child
        right_child = node.right_child

        left_child_height = left_child.height if left_child else -1
        right_child_height = right_child.height if right_child else -1

        if abs(left_child_height - right_child_height) > 1:
            self.rotate(path[0], path[1], path[2])

        self.fix_AVL_property(node.parent, path)

    def remove(self, element):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass


if __name__ == '__main__':

    bst = BinarySearchTree()
    # bst.insert(10, None)
    # bst.insert(8, bst.root)
    # bst.insert(11, bst.root)
    # bst.insert(1, bst.root)
    # bst.insert(3, bst.root)
    # bst.insert(28, bst.root)
    # bst.insert(15, bst.root)

    bst.insert(41, None)
    bst.insert(20, bst.root)
    bst.insert(65, bst.root)
    bst.insert(11, bst.root)
    bst.insert(26, bst.root)
    bst.insert(50, bst.root)
    bst.insert(23, bst.root)
    bst.insert(29, bst.root)
    bst.insert(55, bst.root)
    BinarySearchTree.recursive_print(bst.root, None)


