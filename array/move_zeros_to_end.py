"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""
import unittest


def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
        if i is 0:  # not using `not i` to avoid `False`, `[]`, etc.
            zeros += 1
        else:
            result.append(i)
    
    result.extend([0] * zeros)
    return result


class TestSuite(unittest.TestCase):

    def test_move_zeros(self):

        self.assertListEqual(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]),
                             [False, 1, 1, 2, 1, 3, "a", 0, 0])

        self.assertListEqual(move_zeros([0, 34, 'rahul', [], None, 0, True, 0]),
                             [34, 'rahul', [], None, True, 0, 0, 0])


if __name__ == '__main__':

    unittest.main()
