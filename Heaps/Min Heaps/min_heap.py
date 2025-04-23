# Left child = current_node * 2 
# Right child = current_node * 2 + 1
# Works if first node is counted as 1


class MinHeap:
    def __init__(self, heap: list = []):
        self.min_heap = heap
    

def min_heap_sort(heap: list, current_node_index: int = 0):
    current_node_index += 1
    left_node_index = current_node_index * 2 - 1
    right_node_index = current_node_index * 2

    current_node = heap[current_node_index]
    left_node = heap[left_node_index]
    right_node = heap[right_node_index]

    if max(current_node, left_node, right_node) == current_node:
        min_heap_sort(heap, left_node)
        min_heap_sort(heap, right_node)
        return
    
    if right_node >= left_node:
        current_node, right_node = right_node, current_node
    else:
        current_node, left_node = left_node, current_node
    
    min_heap_sort(heap, left_node)
    min_heap_sort(heap, right_node)
    return