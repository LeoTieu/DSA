# Left child = current_node * 2 
# Right child = current_node * 2 + 1
# Works if first node is counted as 1


class MinHeap:
    '''Takes a list and converts it into a min heap'''    
    def __init__(self, heap: list = None):
        if heap == None:
            heap = []
        self.min_heap = heap
        convert_to_min_heap(self.min_heap)


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

    