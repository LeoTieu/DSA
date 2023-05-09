# Implement a function that checks if a binary tree contains a specific element.

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    
    def contains(self, element):
        '''Checks if element exists within the binary Tree.
        Uses a queue
        '''
        if self.root is None:
            return False
        # A real queue would be better here
        queue = [self.root]
        while len(queue) != 0:
            current = queue.pop(0)
            if current.value == element:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False
    
    
    def contains2(self, target):
        '''Checks if element exists within the binary Tree.
        Uses a recursive method
        '''
        def contains2_recursive(root, target):
            if root is None:
                return False
            if root.value == target:
                return True
            return contains2_recursive(root.left, target) or contains2_recursive(root.right, target)        
        if self.root.value == target:
            return True
        return contains2_recursive(self.root, target)



if __name__ == '__main__':

    #               1
    #           /       \  
    #          2          3  
    #         /  \      /   \
    #        4    5     6    7 

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Iterative")          # Iterative
    print(tree.contains(5))     # True
    print(tree.contains(8))     # False
    print(tree.contains(-23))   # False

    print("Recursive")          # Recursive
    print(tree.contains2(5))    # True
    print(tree.contains2(8))    # False
    print(tree.contains2(-23))  # False