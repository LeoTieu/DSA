import unittest
from random import randint
from min_heap import convert_to_min_heap, MinHeap


class TestMinHeap(unittest.TestCase):
    def test_convert_to_min_heap(self):
        for i in range(10):
            heap = [randint(1,50) for _ in range(randint(30,50))]
            convert_to_min_heap(heap)
            self._assert_is_min_heap(heap)

    
    

    def test_creation_of_min_heap(self):
        for i in range(10):
            heap = [randint(1,50) for _ in range(randint(30,50))]
            min_heap = MinHeap(heap)
            self._assert_is_min_heap(min_heap.min_heap)


    def _assert_is_min_heap(self, heap):
        for i in range(len(heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap):
                self.assertLessEqual(heap[i], heap[left])
            if right < len(heap):
                self.assertLessEqual(heap[i], heap[right])


if __name__ == "__main__":
    unittest.main()
