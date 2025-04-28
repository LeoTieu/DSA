# Left child = current_node * 2 
# Right child = current_node * 2 + 1
# Works if first node is counted as 1


class MinHeap:
    def __init__(self, heap: list = []):
        self.min_heap = heap
    

def min_heap_sort(heap: list, current_node_index: int = 0):
    '''
    Trying to implement a version of min heap
    '''
    current_node = heap[current_node_index]
    left_node_index = current_node_index * 2 + 1
    right_node_index = current_node_index * 2 + 2    


    if left_node_index < len(heap):
        left_node = heap[left_node_index]
        if left_node < current_node:
            heap[left_node_index], heap[current_node_index] = current_node, left_node
            min_heap_sort(heap, left_node_index)


    if right_node_index < len(heap):
        right_node = heap[right_node_index]
        if right_node < current_node:
            heap[right_node_index], heap[current_node_index] = current_node, right_node
            min_heap_sort(heap, right_node_index)
    
    return


if __name__ == '__main__':
    my_heap = [9, 4, 7, 1, -2, 6, 5]
    min_heap_sort(my_heap)
    print("sorted heap = ", my_heap)