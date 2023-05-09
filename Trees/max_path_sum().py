# Implement a "Max Root To Leaf Path Sum" function
# Code heavily inspired by min_value().py

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    

    def max_path_sum(self):
        '''Finds the maximum value path within the binary tree.
        Uses a recursive method.
        '''
        def max_path_sum_recursive(node):
            if node.left is None and node.right is None:
                return node.value
            right_max = max_path_sum_recursive(node.right)
            left_max = max_path_sum_recursive(node.left)
            return max(right_max, left_max) + node.value
        return max_path_sum_recursive(self.root)
    
if __name__ == '__main__':

    #               1
    #           /       \  
    #          2          3  
    #         /  \      /   \
    #        4    5     6   7 

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.max_path_sum())      # 11