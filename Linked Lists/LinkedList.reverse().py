# Write a function to reverse the elements in the linked list.
# Function has a time complexity of O(N)

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, lst=None):
        self.head = node()
        if lst is not None:
            for elem in lst:
                self.append(elem)
    

    def reverse(self):
        '''
        Reverses elements within the linked list
        '''
        cur_node = self.head.next
        past_node = None
        second_last_node = None
        while cur_node is not None:
            second_last_node = past_node
            past_node = cur_node
            cur_node = cur_node.next
            past_node.next = second_last_node
        self.head.next = past_node


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
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

if __name__ == '__main__':
    MyLinkedList = linked_list(["f", "d", "g", "h", "o"])
    MyLinkedList.reverse()
    MyLinkedList.display() # Output ['o', 'h', 'g', 'd', 'f']