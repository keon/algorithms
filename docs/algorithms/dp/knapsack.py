"""
Given the capacity of the knapsack and items specified by weights and values,
return the maximum summarized value of the items that can be fit in the
knapsack.

Example:
capacity = 5, items(value, weight) = [(60, 5), (50, 3), (70, 4), (30, 2)]
result = 80 (items valued 50 and 30 can both be fit in the knapsack)

The time complexity is O(n * m) and the space complexity is O(m), where n is
the total number of items and m is the knapsack's capacity.
"""


class Item:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def get_maximum_value(items, capacity):
    dp = [0] * (capacity + 1)
    for item in items:
        for cur_weight in reversed(range(item.weight, capacity+1)):
            dp[cur_weight] = max(dp[cur_weight], item.value + dp[cur_weight - item.weight])
    return dp[capacity]

