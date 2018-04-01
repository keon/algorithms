"""
Given a non-negative number represented as an array of digits,
plus one to the number.

The digits are stored such that the most significant
digit is at the head of the list.
"""
import unittest


def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        summ = 0
        if i >= 0:
            summ += digits[i]
        if ten:
            summ += 1
        res.append(summ % 10)
        ten = summ // 10
        i -= 1
    return res[::-1]


def plus_one_v2(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


def plus_one_v3(num_arr):

    for idx, digit in reversed(list(enumerate(num_arr))):
        num_arr[idx] = (num_arr[idx] + 1) % 10
        if num_arr[idx]:
            return num_arr
    return [1] + num_arr


class TestSuite(unittest.TestCase):

    def test_plus_one(self):

        self.assertListEqual(plus_one([0]), [1])
        self.assertListEqual(plus_one([9]), [1, 0])
        self.assertListEqual(plus_one([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one([9, 9, 8, 0, 0, 9]), [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one([9, 9, 9, 9]), [1, 0, 0, 0, 0])

    def test_plus_one_v2(self):

        self.assertListEqual(plus_one_v2([0]), [1])
        self.assertListEqual(plus_one_v2([9]), [1, 0])
        self.assertListEqual(plus_one_v2([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 8, 0, 0, 9]), [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v2([9, 9, 9, 9]), [1, 0, 0, 0, 0])

    def test_plus_one_v3(self):

        self.assertListEqual(plus_one_v3([0]), [1])
        self.assertListEqual(plus_one_v3([9]), [1, 0])
        self.assertListEqual(plus_one_v3([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 8, 0, 0, 9]), [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one_v3([9, 9, 9, 9]), [1, 0, 0, 0, 0])


if __name__ == '__main__':

    unittest.main()