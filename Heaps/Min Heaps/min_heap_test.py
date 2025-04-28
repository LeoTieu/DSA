import unittest
from min_heap import min_heap_sort

class TestMinHeap(unittest.TestCase):
    def test_min_heap_property(self):
        heap = [9, 4, 7, 1, -2, 6, 5]
        min_heap_sort(heap)
        print("sorted heap = ", heap)

        for i in range(len(heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap):
                self.assertLessEqual(heap[i], heap[left])
            if right < len(heap):
                self.assertLessEqual(heap[i], heap[right])

if __name__ == "__main__":
    unittest.main()
