from algorithms.sort import (
    bitonic_sort,
    bogo_sort,
    bubble_sort,
    comb_sort,
    counting_sort,
    cycle_sort,
    exchange_sort,
    max_heap_sort, min_heap_sort,
    merge_sort,
    pancake_sort,
    pigeonhole_sort,
    quick_sort,
    selection_sort,
    bucket_sort,
    shell_sort,
    radix_sort,
    gnome_sort,
    cocktail_shaker_sort,
    top_sort, top_sort_recursive,
    stoogesort
)

import unittest


def is_sorted(array):
    """
    Helper function to check if the given array is sorted.
    :param array: Array to check if sorted
    :return: True if sorted in ascending order, else False
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


class TestSuite(unittest.TestCase):
    def test_bogo_sort(self):
        self.assertTrue(is_sorted(bogo_sort([1, 23, 5])))

    def test_bitonic_sort(self):
        self.assertTrue(is_sorted(bitonic_sort([1, 3, 2, 5, 65,
                                                23, 57, 1232])))

    def test_bubble_sort(self):
        self.assertTrue(is_sorted(bubble_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_comb_sort(self):
        self.assertTrue(is_sorted(comb_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_counting_sort(self):
        self.assertTrue(is_sorted(counting_sort([1, 3, 2, 5, 65,
                                                 23, 57, 1232])))

    def test_cycle_sort(self):
        self.assertTrue(is_sorted(cycle_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_exchange_sort(self):
        self.assertTrue(is_sorted(exchange_sort([1, 3, 2, 5, 65,
                                                 23, 57, 1232])))

    def test_heap_sort(self):
        self.assertTrue(is_sorted(max_heap_sort([1, 3, 2, 5, 65,
                                                 23, 57, 1232])))

        self.assertTrue(is_sorted(min_heap_sort([1, 3, 2, 5, 65,
                                                 23, 57, 1232])))

    def test_insertion_sort(self):
        self.assertTrue(is_sorted(bitonic_sort([1, 3, 2, 5, 65,
                                                23, 57, 1232])))

    def test_merge_sort(self):
        self.assertTrue(is_sorted(merge_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_pancake_sort(self):
        self.assertTrue(is_sorted(pancake_sort([1, 3, 2, 5, 65,
                                                23, 57, 1232])))

    def test_pigeonhole_sort(self):
        self.assertTrue(is_sorted(pigeonhole_sort([1, 5, 65, 23, 57, 1232])))

    def test_quick_sort(self):
        self.assertTrue(is_sorted(quick_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_selection_sort(self):
        self.assertTrue(is_sorted(selection_sort([1, 3, 2, 5, 65,
                                                  23, 57, 1232])))

    def test_bucket_sort(self):
        self.assertTrue(is_sorted(bucket_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_shell_sort(self):
        self.assertTrue(is_sorted(shell_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_radix_sort(self):
        self.assertTrue(is_sorted(radix_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_gnome_sort(self):
        self.assertTrue(is_sorted(gnome_sort([1, 3, 2, 5, 65, 23, 57, 1232])))

    def test_cocktail_shaker_sort(self):
        self.assertTrue(is_sorted(cocktail_shaker_sort([1, 3, 2, 5, 65,
                                                        23, 57, 1232])))


class TestTopSort(unittest.TestCase):
    def setUp(self):
        self.depGraph = {
                            "a": ["b"],
                            "b": ["c"],
                            "c": ['e'],
                            'e': ['g'],
                            "d": [],
                            "f": ["e", "d"],
                            "g": []
                        }

    def test_topsort(self):
        res = top_sort_recursive(self.depGraph)
        # print(res)
        self.assertTrue(res.index('g') < res.index('e'))
        res = top_sort(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))
class TestStoog(unittest.TestCase):
    def test_stoogesort(self):
        arr1 = [1, 3, 64, 5, 7, 8]
        stoogesort(arr1, 0, len(arr1) - 1)
        self.assertEqual(arr1, [1, 3, 5, 7, 8, 64])

        arr2 = [5, 4, 3, 2, 1]
        stoogesort(arr2, 0, len(arr2) - 1)
        self.assertEqual(arr2, [1, 2, 3, 4, 5])

        arr3 = [1, 2, 3, 4, 5]
        stoogesort(arr3, 0, len(arr3) - 1)
        self.assertEqual(arr3, [1, 2, 3, 4, 5])

        arr4 = [10, -1, 2, 3, 0]
        stoogesort(arr4, 0, len(arr4) - 1)
        self.assertEqual(arr4, [-1, 0, 2, 3, 10])

        arr5 = []
        stoogesort(arr5, 0, len(arr5) - 1)
        self.assertEqual(arr5, [])

if __name__ == "__main__":
    unittest.main()
