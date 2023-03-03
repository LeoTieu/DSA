# Code taken from: https://github.com/bfaure/Python3_Data_Structures/blob/master/Linked_List/main.py

# A linked list is to my understanding, a node with data + a pointer to the next node.
# We can therefore change elements inside of a linked list or extend it with a linear time.


# Imporvable parts on the code: A few error messages
class node:
    '''
    User will never touch this class
    Subclass of linked list
    '''

    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        # Used as a placeholder to allow us to point to the first element in the list.
        self.head = node()


    def append(self, data):
        '''
        Appends data to end of list
        '''
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node


    def __len__(self):
        """
        Gets length of list
        """
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    

    def display(self):
        '''
        Displays elements in a list format
        '''
        elements = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)


    def get(self,index):
        """
        Returns element by index
        """

        if not index <= self.size:
            raise IndexError(f'Given index: {index} is larger than array size {self.size}')
        
        cur_idx= 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx+=1

    def erase(self, index):
        '''
        Erases element by index
        '''
        if not 0 <= index < self.size:
            raise IndexError(f'Given index: {index} is larger than array size {self.size}')
        
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

    # Allows for bracket operator syntax (i.e. a[0] to return first item)
    # Whatever that means
    def __getitem__(self, index):
        '''
        Gets item
        '''
        return self.get(index)
    

    # Inserts a new node at index 'index' containing data 'data'.
	# Indices begin at 0. If the provided index is greater than or 
	# equal to the length of the linked list the 'data' will be appended.
    def insert(self, index, data):
        '''
        Inserts data by index
        '''
        if index < 0:
            print("Error: 'Erase' Index cannot be negative!")
            return
        if index >= self.length(): # Append the node
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next=node
            return
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                prior_node.next=node
                return
            prior_node = cur_node
            cur_idx += 1

    # Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal 
	# to the length of the linked list a warning will be printed 
	# to the user.
    def set(self, index, data):
        '''
        Pretty sure this doesn't even work
        Sets data by index
        '''
        if index >= self.length() or index <0:
            print("Error: 'Set' Index out of range!")
            return
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                return
        cur_idx += 1
