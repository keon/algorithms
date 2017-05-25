"""
Say you have an array for which the ith element
is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


# O(n^2) time
def max_profit_naive(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_so_far = 0
    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_so_far = max(max_so_far, prices[j] - prices[i])
    return max_so_far


# O(n) time
def max_profit_optimized(prices):
    """
    input: [7, 1, 5, 3, 6, 4]
    diff : [X, -6, 4, -2, 3, -2]
    :type prices: List[int]
    :rtype: int
    """
    cur_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i-1])
        max_so_far = max(max_so_far, cur_max)
    return max_so_far
