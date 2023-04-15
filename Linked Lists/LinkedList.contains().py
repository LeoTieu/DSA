# Write a function to check if an element is present in the linked list.
# Function has a time complexity of O(N)

class node:
    '''
    User will never touch this class
    Subclass of linked list
    '''

    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def contains(self, element):
        '''
        Checks if an element exists within the linked list
        '''
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == element:
                return True
            cur_node = cur_node.next
        return False


    def __init__(self, lst=None):
        self.head = node()
        if lst is not None:
            for elem in lst:
                self.append(elem)
    

    def display(self):
        '''
        Displays elements in a list format
        '''
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def append(self, data):
        '''
        Appends data to end of list
        '''
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

if __name__ == '__main__':
    MyLinkedList = linked_list(["f", "d", "g", "h", "o"])
    print(MyLinkedList.contains("e"))
    # False
    print(MyLinkedList.contains("d"))
    # True