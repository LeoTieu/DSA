import unittest
from min_heap import min_heap_sort

class TestMinHeap(unittest.TestCase):
    def test_min_heap_property(self):
        input_list = [9, 4, 7, 1, -2, 6, 5]
        heap = min_heap_sort(input_list)

        for i in range(len(heap.min_heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap.min_heap):
                self.assertLessEqual(heap.min_heap[i], heap.min_heap[left])
            if right < len(heap.min_heap):
                self.assertLessEqual(heap.min_heap[i], heap.min_heap[right])

if __name__ == "__main__":
    unittest.main()
