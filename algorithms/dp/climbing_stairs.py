"""
You are climbing a stair case.
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


# O(n) space

def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    arr = [1, 1]
    for _ in range(1, n):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]


# the above function can be optimized as:
# O(1) space

def climb_stairs_optimized(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
