# Current min_heap


class MinHeap:
    '''Min heap datastructure meant soley for learning'''    
    def __init__(self, heap: list = None):
        if heap == None:
            heap = []
        self.min_heap = heap
        convert_to_min_heap(self.min_heap)


    def get_min(self) -> int:
        '''Gets the minimum value in the min heap'''
        return self.heap[0]


    def extract_min(self) -> int:
        '''
        Gets the minimum value in the min heap and removes it
        Keeps the min heap structure
        '''
        minimum = self.min_heap[0]
        self.min_heap[0] = self.min_heap[-1]
        self.min_heap.pop()
        min_heapify(self.min_heap)

        return minimum


    def insert(self, number: int) -> None:
        self.min_heap.append(number)
        current_index = len(self.min_heap) - 1
        
        self._bottom_up_heapify(current_index)

    def _bottom_up_heapify(self, child_index):
        if child_index == 0:
            return

        parent_index = (child_index-1)//2
        if self.min_heap[child_index] < self.min_heap[parent_index]:
            self.min_heap[child_index], self.min_heap[parent_index] = self.min_heap[parent_index], self.min_heap[child_index]
            self._bottom_up_heapify(parent_index)
        return
    
    def __len__(self):
        return len(self.min_heap)


def min_heapify(heap: list, current_node_index: int = 0):
    left_node_index = current_node_index * 2 + 1
    right_node_index = current_node_index * 2 + 2    


    if left_node_index < len(heap):
        if heap[left_node_index] < heap[current_node_index]:
            heap[left_node_index], heap[current_node_index] = heap[current_node_index], heap[left_node_index]
            min_heapify(heap, left_node_index)


    if right_node_index < len(heap):
        if heap[right_node_index] < heap[current_node_index]:
            heap[right_node_index], heap[current_node_index] = heap[current_node_index], heap[right_node_index]
            min_heapify(heap, right_node_index)
    return


def convert_to_min_heap(heap: list):
    for i in range(len(heap) // 2 - 1, -1, -1):
        min_heapify(heap, i)
