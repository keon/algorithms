from algorithms.heap import (
    BinaryHeap,
    get_skyline,
    max_sliding_window
)

import unittest

class TestBinaryHeap(unittest.TestCase):
    """
        Test suite for the binary_heap data structures
    """
    def setUp(self):
        self.min_heap = BinaryHeap()
        self.min_heap.insert(4)
        self.min_heap.insert(50)
        self.min_heap.insert(7)
        self.min_heap.insert(55)
        self.min_heap.insert(90)
        self.min_heap.insert(87)

    def test_insert(self):
        # Before insert 2: [0, 4, 50, 7, 55, 90, 87]
        # After insert:  [0, 2, 50, 4, 55, 90, 87, 7]
        self.min_heap.insert(2)
        self.assertEqual([0, 2, 50, 4, 55, 90, 87, 7],
                          self.min_heap.heap)
        self.assertEqual(7, self.min_heap.currentSize)

    def test_remove_min(self):
        ret = self.min_heap.remove_min()
        # Before remove_min : [0, 4, 50, 7, 55, 90, 87]
        # After remove_min: [7, 50, 87, 55, 90]
        # Test return value
        self.assertEqual(4,ret)
        self.assertEqual([0, 7, 50, 87, 55, 90],
                          self.min_heap.heap)
        self.assertEqual(5, self.min_heap.currentSize)

class TestSuite(unittest.TestCase):
    def test_get_skyline(self):
        buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], \
                      [15, 20, 10], [19, 24, 8] ]
        # Expect output
        output = [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], \
                   [20, 8], [24, 0] ]
        self.assertEqual(output, get_skyline(buildings))

    def test_max_sliding_window(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual([3, 3, 5, 5, 6, 7], max_sliding_window(nums, 3))

if __name__ == "__main__":
    unittest.main()
