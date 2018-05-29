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


class Item(object):

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def get_maximum_value(items, capacity):
    dp = [0] * (capacity + 1)
    for item in items:
        dp_tmp = [total_value for total_value in dp]
        for current_weight in range(capacity + 1):
            total_weight = current_weight + item.weight
            if total_weight <= capacity:
                dp_tmp[total_weight] = max(dp_tmp[total_weight],
                                           dp[current_weight] + item.value)
        dp = dp_tmp
    return max(dp)


print(get_maximum_value([Item(60, 10), Item(100, 20), Item(120, 30)],
                        50))
print(get_maximum_value([Item(60, 5), Item(50, 3), Item(70, 4), Item(30, 2)],
                        5))
