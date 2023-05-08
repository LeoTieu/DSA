# Code and video - https://www.youtube.com/watch?v=6oL-0TdVy28&t (12 mars 2018)
# Publisher - Vincent Russo
# Channel - LucidProgramming

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")[:-1:]
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")[:-1:]
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")[:-1:]
        else:
            print(f"Traversal type {traversal_type} is not supported.")
            return False

    def preorder(self, start, traversal):
        '''Root -> Left -> Right'''
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal):
        '''Left -> Root -> Right'''
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    
    def postorder(self, start, traversal):
        '''Left -> Right -> Root'''
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal




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
    print(tree.print_tree("inorder")) # 4-2-5-1-6-3-7
    print(tree.print_tree("postorder")) # 4-2-5-6-3-7-1
