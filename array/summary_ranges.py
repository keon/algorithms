"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""
import unittest


def summary_ranges(array):
    """
    :type array: List[int]
    :rtype: List[]
    """
    res = []
    if len(array) == 1:
        return [str(array[0])]
    i = 0
    while i < len(array):
        num = array[i]
        while i + 1 < len(array) and array[i + 1] - array[i] == 1:
            i += 1
        if array[i] != num:
            res.append((num, array[i]))
        else:
            res.append((num, num))
        i += 1
    return res


class TestSuite(unittest.TestCase):

    def test_summary_ranges(self):

        self.assertListEqual(summary_ranges([0, 1, 2, 4, 5, 7]),
                             [(0, 2), (4, 5), (7, 7)])
        self.assertListEqual(summary_ranges([-5, -4, -3, 1, 2, 4, 5, 6]),
                             [(-5, -3), (1, 2), (4, 6)])
        self.assertListEqual(summary_ranges([-2, -1, 0, 1, 2]),
                             [(-2, 2)])


if __name__ == '__main__':

    unittest.main()