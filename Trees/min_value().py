# Implement a function that finds the smallest value in a binary tree.
# Code translated to python from the video:
# Binary Tree Algorithms for Technical Interviews - Full Course (18 oct. 2021)
# Publisher - Alvin Zablan
# Channel - freeCodeCamp.org

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root=None):
        self.root = Node(root)
    

    def min_value(self):
        '''Finds minimum value within the binary tree'''
        if self.root is None:
            return
        def min_value_recursive(node):
            if node == None:
                return(float("inf"))
            left_min = min_value_recursive(node.left)
            right_min = min_value_recursive(node.right)
            return min(node.value, left_min, right_min)
        return(min_value_recursive(self.root))
        


if __name__ == '__main__':
    # Set up tree:
    tree = BinaryTree(6556)
    tree.root.left = Node(1233)
    tree.root.right = Node(454)
    tree.root.left.left = Node(321)
    tree.root.left.right = Node(123)
    tree.root.right.left = Node(500)
    tree.root.right.right = Node(843)
    tree.root.right.right.right = Node(1255)
    tree.root.right.right.right.right = Node(432)
    tree.root.right.right.right.right.right = Node(1203)
    print(tree.min_value())     # 123