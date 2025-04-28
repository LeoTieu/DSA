import unittest
from random import randint

from min_heap import min_heap_sort


class TestMinHeap(unittest.TestCase):
    def test_min_heap_property(self):
        for i in range(10):
            heap = [randint(1,50) for _ in range(30)]
            min_heap_sort(heap)

            for i in range(len(heap)):
                left = 2 * i + 1
                right = 2 * i + 2

                if left < len(heap):
                    self.assertLessEqual(heap[i], heap[left])
                if right < len(heap):
                    self.assertLessEqual(heap[i], heap[right])

if __name__ == "__main__":
    unittest.main()
