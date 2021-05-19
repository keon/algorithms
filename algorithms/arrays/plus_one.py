"""
Given a non-negative number represented as an array of digits,
adding one to each numeral.

The digits are stored big-endian, such that the most significant
digit is at the head of the list.
"""


def plusOneV1(digits):
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


def plusOneV2(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


def plusOneV3(numAarr):

    for idx in reversed(list(enumerate(numArr))):
        numArr[idx[0]] = (numArr[idx[0]] + 1) % 10
        if numArr[idx[0]]:
            return numArr
    return [1] + numArr
