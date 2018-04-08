import unittest
def insertion_sort(arr):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos-1]
            pos = pos-1
        # Break and do the final swap
        arr[pos] = cursor
     
    return arr

class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_insertion_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         insertion_sort([1, 5, 65, 23, 57, 1232]))

if __name__ == "__main__":
    unittest.main()
