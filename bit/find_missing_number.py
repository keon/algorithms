def find_missing_number(nums):
    """Returns the missing number from a sorted list of unique
    integers in range [0..n] in O(n) time and space. The difference
    between consecutive integers cannot be more than 1.

    >>> find_missing_number([i for i in range(0, 10000) if i != 1234])
    1234
    """

    missing = 0
    for i, num in enumerate(nums):
        missing ^= num
        missing ^= i + 1

    return missing
