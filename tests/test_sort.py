from algorithms.sort import (
    bitonic_sort,
    bogo_sort,
    bubble_sort,
    comb_sort,
    counting_sort,
    cycle_sort,
    max_heap_sort, min_heap_sort,
    insertion_sort,
    merge_sort,
    pancake_sort,
    quick_sort,
    selection_sort,
    bucket_sort,
    shell_sort,
    radix_sort,
    gnome_sort,
    cocktail_shaker_sort,
    top_sort, top_sort_recursive
)

import unittest


class TestSuite(unittest.TestCase):
    def test_bogo_sort(self):
        self.assertEqual([1, 5, 23],
                         bogo_sort([1, 23, 5]))

    def test_bitonic_sort(self):
        self.assertEqual([1, 2, 3, 5, 23, 57, 65, 1232],
                         bitonic_sort([1, 3, 2, 5, 65, 23, 57, 1232]))
        self.assertEqual([1, 2, 3, 5, 23, 57, 65, 1232],
                         bitonic_sort([1, 3, 2, 5, 65, 23, 57, 1232],False))
        self.assertEqual([1232, 65, 57, 23, 5, 3, 2, 1],
                         bitonic_sort([1, 2, 3, 5, 65, 23, 57, 1232],True))

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

    def test_cycle_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         cycle_sort([1, 5, 65, 23, 57, 1232]))

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

    def test_pancake_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         pancake_sort([1, 5, 65, 23, 57, 1232]))

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

    def test_radix_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                        radix_sort([1, 5, 65, 23, 57, 1232]))

    def test_gnome_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         gnome_sort([1, 5, 65, 23, 57, 1232]))

    def test_cocktail_shaker_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                        cocktail_shaker_sort([1, 5, 65, 23, 57, 1232]))

class TestTopSort(unittest.TestCase):
    def setUp(self):
        self.depGraph = {
                            "a" : [ "b" ],
                            "b" : [ "c" ],
                            "c" :  [ 'e'],
                            'e' : [ 'g' ],
                            "d" : [ ],
                            "f" : ["e" , "d"],
                            "g" : [ ]
                        }

    def test_topsort(self):
        res = top_sort_recursive(self.depGraph)
        #print(res)
        self.assertTrue(res.index('g') < res.index('e'))
        res = top_sort(self.depGraph)
        self.assertTrue(res.index('g') < res.index('e'))


if __name__ == "__main__":
    unittest.main()
