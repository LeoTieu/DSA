# Implement a function to find the depth of a Binary tree

# Personal Comments:
# Can't create an empty Binary tree.
# It works on leetcode tho
# See line 52 for issue.

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root=None):
        self.root = Node(root)

    
    def depth(self):  
        def depth_recursive(start):
            if start:
                return max(depth_recursive(start.left), depth_recursive(start.right)) + 1
            else:
                return 0
        return depth_recursive(self.root)
        




if __name__ == '__main__':

    #               1
    #           /       \  
    #          2         3  
    #         / \       / \
    #        4   5     6   7 (- 6 - 2- 1)

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(6)
    tree.root.right.right.right.right = Node(2)
    tree.root.right.right.right.right.right = Node(1)
    print(tree.depth())     # 6
    tree2 = BinaryTree()
    print(tree2.depth())    # 1 (Should be 0)