# Write a function to remove the first occurrence of an element from the linked list.
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
    def remove_first(self, element):
        '''
        Removes first occurrence
        '''
        cur_node = self.head
        last_node = None
        while cur_node is not None:
            last_node = cur_node
            cur_node = cur_node.next
            print(cur_node.data)
            if cur_node.data == element:
                last_node.next = cur_node.next
                return


    def __init__(self, lst=None):
        self.head = node()
        if lst is not None:
            for elem in lst:
                self.append(elem)


    def append(self, data):
        '''
        Appends data to end of list
        '''
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node


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


if __name__ == '__main__':
    MyLinkedList = linked_list(["f", "d", "g", "h", "o"])

    MyLinkedList.append("h")
    MyLinkedList.remove_first("h")
    MyLinkedList.display() # Output ['f', 'd', 'g', 'o', 'h']