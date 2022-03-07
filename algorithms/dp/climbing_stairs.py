"""
You are climbing a stair case.
It takes `steps` number of steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given argument `steps` will be a positive integer.
"""


# O(n) space

def climb_stairs(steps):
    """
    :type steps: int
    :rtype: int
    """
    arr = [1, 1]
    for _ in range(1, steps):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]


# the above function can be optimized as:
# O(1) space

def climb_stairs_optimized(steps):
    """
    :type steps: int
    :rtype: int
    """
    a_steps = b_steps = 1
    for _ in range(steps):
        a_steps, b_steps = b_steps, a_steps + b_steps
    return a_steps
