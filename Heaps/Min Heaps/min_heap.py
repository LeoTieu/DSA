# Left child = current_node * 2 
# Right child = current_node * 2 + 1
# Works if first node is counted as 1


class MinHeap:
    def __init__(self, heap: list = None):
        if heap == None:
            heap = []
        self.min_heap = heap
    

def min_heapify(heap: list, current_node_index: int = 0):
    current_node = heap[current_node_index]
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


def min_heap_sort(heap: list):
    for i in range(len(heap) // 2 - 1, -1, -1):
        print(i)
        min_heapify(heap, i)


if __name__ == '__main__':
    my_heap = [9, 4, 7, 1, -2, 6, 5]
    # my_heap = [7,6,5,4,3,2,1]
    min_heap_sort(my_heap)
    print("sorted heap = ", my_heap)