"""
Problem
Given a value `value`, if we want to make change for `value` cents, and we have infinite
supply of each of coins = {S1, S2, .. , Sm} valued `coins`, how many ways can we make the change?
The order of `coins` doesn't matter.
For example, for `value` = 4 and `coins` = [1, 2, 3], there are four solutions:
[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
So output should be 4.

For `value` = 10 and `coins` = [2, 5, 3, 6], there are five solutions:

[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].
So the output should be 5.

Time complexity: O(n * m) where n is the `value` and m is the number of `coins`
Space complexity: O(n)
"""

def count(coins, value):
    """ Find number of combination of `coins` that adds upp to `value`

    Keyword arguments:
    coins -- int[]
    value -- int
    """
    # initialize dp array and set base case as 1
    dp_array = [1] + [0] * value

    # fill dp in a bottom up manner
    for coin in coins:
        for i in range(coin, value+1):
            dp_array[i] += dp_array[i-coin]

    return dp_array[value]
