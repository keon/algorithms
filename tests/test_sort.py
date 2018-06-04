from algorithms.sort import (
    bubble_sort,
    comb_sort,
    counting_sort,
    max_heap_sort, min_heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
    bucket_sort,
    shell_sort
)

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
                         quick_sort([1, 5, 65, 23, 57, 1232]))

    def test_selection_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         selection_sort([1, 5, 65, 23, 57, 1232]))

    def test_bucket_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                        bucket_sort([1, 5, 65, 23, 57, 1232]))

    def test_shell_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                        shell_sort([1, 5, 65, 23, 57, 1232]))
                                          


if __name__ == "__main__":
    unittest.main()
