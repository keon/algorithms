def find_missing_number(nums):
    """Returns the missing number from a sorted sequence of integers
    in O(n) time and space.

    >>> find_missing(i for i in range(-2000, 10000) if i != 1234)
    1234
    """

    # Ensure indexable
    nums = list(nums)

    # Force odd length
    if len(nums) & 1 == 0:
        nums.append(nums[-1] + 1)

    missing = 0
    for i, num in enumerate(nums):
        if num != 0:
            missing ^= num
        missing ^= i + 1

    return missing
