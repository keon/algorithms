import unittest
def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)
    return arr
def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_quick_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         quick_sort([1, 5, 65, 23, 57, 1232], 0, 5))

if __name__ == "__main__":
    unittest.main()
