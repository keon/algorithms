import unittest


def selection_sort(arr):
    """ Selection Sort
        Complexity: O(n^2)
    """
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


class TestSuite(unittest.TestCase):
    """
        test suite for the function (above)
    """
    def test_selection_sort(self):
        self.assertEqual([1, 5, 23, 57, 65, 1232],
                         selection_sort([1, 5, 65, 23, 57, 1232]))

        
if __name__ == "__main__":
    unittest.main()
