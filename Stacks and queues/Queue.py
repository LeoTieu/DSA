# Queue made by me.
# A lot of code taken from DynamicArrays.py

# A queue is well, a queue
# First in and first out
# This implementation can store N elements where N = Array length
# Adding and removing from queue in O(1) time complexity

class queue:
    """
    Self implementation of a python queue
    """
    def __init__(self):
        # Number of elements in the queue
        self.size = 0
        # Maximum size of the queue
        self.capacity = 1
        # The queue
        self.queue = self._create_queue(self.capacity)
        # Last element pointer
        self.end_pointer = 0
        # First element pointer
        self.beginning_pointer = 0


    def __len__(self):
        '''
        len(queue) Returns the length of the queue
        '''
        return self.size
    
    
    def __getitem__(self, index):
        '''
        Returns element by index
        '''
        if not index <= self.capacity:
            raise IndexError(f"Given index: {index} is larger than queue size {self.size}")

        return self.queue[index]
    

    def display(self):
        '''
        Displays the current queue
        '''
        elements = []
        for index in range(0, self.capacity):
            elements.append(self.queue[index])
        print(elements)
        print(f"First in queue {self.queue[self.beginning_pointer]}")


    def _create_queue(self, length):
        return [None] * length


    def _resize(self, new_capacity):
        '''
        Resizes the queue
        '''
        new_queue = self._create_queue(new_capacity)

        # Adds element from old queue to new queue
        for i in range(self.size):
            new_queue[i] == self.queue[i]

        self.queue = new_queue
        self.capacity = new_capacity

    
    def addRight(self, element):
        '''
        Adds element to the end of the queue
        '''
        if self.size == self.capacity:
            raise Exception("Can't add to a full list!")

        self.queue[self.end_pointer] = element
        if self.end_pointer == self.capacity - 1:
            self.end_pointer = 0
        else:
            self.end_pointer += 1
        self.size += 1
    

    def removeLeft(self):
        '''
        Removes element at the beginning of the queue
        Returns element at the beginning of the queue
        '''
        removedElement = self.queue[self.beginning_pointer]
        self.queue[self.beginning_pointer] = None

        if self.beginning_pointer == self.capacity:
            self.beginning_pointer = 0
        else:
            self.beginning_pointer +=1
        self.size -= 1
        
        return removedElement
        


if __name__ == '__main__':
    # Testing to see if stuff works
    MyQueue = queue()
    MyQueue._resize(3)
    MyQueue.addRight("Leo0")
    MyQueue.addRight("Leo1")
    MyQueue.addRight("Leo2")
    MyQueue.removeLeft()
    MyQueue.addRight("Leo3")
    MyQueue.display()