# Code taken from: https://medium.com/swlh/data-structure-and-algorithms-implement-dynamic-array-in-python-be47e1d6ce06
# Runtime math: https://www.youtube.com/watch?v=Ij7NQ-0mIVA (cool vid)

# A dynamic array is an array that does NOT have a fixed size.
# And we can therefore append elements into the array.

# Things to add: pop an item in the middle of the array
class DynamicArray():
    def __init__(self):
        # Current number of elements in the array
        self.size = 0
        # Maximum size of the dynamic array
        self.capacity = 1
        # The array
        self.array = self._create_array(self.capacity)

    
    def __len__(self):
        '''
        len(array)Returns the length of the array
        '''
        return self.size


    def __getitem__(self, index):
        '''
        Returns element by index
        '''
        # old (if not 0 <= index < self.size)
        if not index <= self.size:
            raise IndexError(f'Given index: {index} is larger than array size {self.size}')

        return self.array[index]

    
    def _create_array(self, length):
        '''
        Creates an array with a given size
        '''
        return [None] * length


    def _resize(self, new_capacity):
        '''
        Resizes the array to the new array
        '''
        new_array = self._create_array(new_capacity)

        # Adds elements from old array to new array
        for i in range(self.size):
            new_array[i] == self.array[i]

        self.array = new_array
        self.capacity = new_capacity
    

    def append(self, element):
        '''
        Adds new element to array
        '''
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = element
        self.size += 1


    def pop(self):
        '''
        Pops the last element of the array
        '''
        element = None

        if self.size > 0:
            element = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1
        
        if self.size < self.capacity // 2:
            self._resize(self.capacity // 2)
        
        return element


if __name__ == '__main__':
    # Testing to see if stuff works
    Array = DynamicArray()
    Array._resize(3)
    Array.append("Testing0")
    Array.append("Testing1")
    Array.append("Testing2")
    for x in range(0,3):
        print(Array[x])
    Array.pop()
    print(Array[2])
