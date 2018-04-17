from bubble_sort import bubble_sort
from comb_sort import comb_sort
from counting_sort import counting_sort
from heap_sort import max_heap_sort, min_heap_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

import unittest

class TestSuite(unittest.TestCase):
        def test_bubble_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             bubble_sort([1, 5, 65, 23, 57, 1232]))

        def test_comb_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             comb_sort([1, 5, 65, 23, 57, 1232]))

        def test_counting_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             counting_sort([1, 5, 65, 23, 57, 1232]))
            self.assertEqual([-1232, -65, -57, -23, -5, -1],
                             counting_sort([-1, -5, -65, -23, -57, -1232]))

        def test_heap_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             max_heap_sort([1, 5, 65, 23, 57, 1232]))
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             min_heap_sort([1, 5, 65, 23, 57, 1232]))

        def test_insertion_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             insertion_sort([1, 5, 65, 23, 57, 1232]))

        def test_merge_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             merge_sort([1, 5, 65, 23, 57, 1232]))

        def test_quick_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             quick_sort([1, 5, 65, 23, 57, 1232], 0, 5))

        def test_selection_sort(self):
            self.assertEqual([1, 5, 23, 57, 65, 1232],
                             selection_sort([1, 5, 65, 23, 57, 1232]))

if __name__ == "__main__":
    unittest.main()
