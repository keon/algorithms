def find_missing_number(nums):
    """Returns the missing number from a sequence of unique integers
    in range [0..n] in O(n) time and space. The difference between
    consecutive integers cannot be more than 1. If the sequence is
    already complete, the next integer in the sequence will be returned.

    >>> find_missing_number(i for i in range(0, 10000) if i != 1234)
    1234
    >>> find_missing_number([4, 1, 3, 0, 6, 5, 2])
    7
    """

    missing = 0
    for i, num in enumerate(nums):
        missing ^= num
        missing ^= i + 1

    return missing
