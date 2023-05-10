# Implement a function that reverses a binary tree

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")[:-1:]


    def preorder(self, start, traversal):
        '''Root -> Left -> Right'''
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    

    def reverse(self):
        '''Reverses the binary tree
        Uses a recursive method. 
        '''
        def reverse_node(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            reverse_node(node.left)
            reverse_node(node.right)
        reverse_node(self.root)


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

    print(tree.print_tree("preorder")) # 1-2-4-5-3-6-7-8
    tree.reverse()

    #               1
    #           /       \  
    #          3          2  
    #         /  \      /   \
    #        7    6     5   4 
    
    print(tree.print_tree("preorder")) # 1-3-7-6-2-5-4