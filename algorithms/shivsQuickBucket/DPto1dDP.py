from functools import cache

# 2D DP
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        @cache
        def recursion(prev, curri):
            if not curri < len(prices): return 0

            profit = 0
            if not prev:
                profit = max(recursion(prev, curri + 1), recursion(prices[curri], curri + 1))
            elif prices[curri] > prev:
                profit = max((prices[curri] - prev - fee) + recursion(0, curri + 1), recursion(prev, curri + 1))
            else:
                profit = recursion(prev, curri + 1)
            return profit
        return recursion(0, 0)

# Converted to 1D DP
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        @cache
        def recursion(curri, b):
            if curri == len(prices): return 0

            if b:
                buy = recursion(curri + 1, 0) - prices[curri] - fee
                notBuy = recursion(curri + 1, 1)
                return max(buy, notBuy)
            
            sell = recursion(curri + 1, 1) + prices[curri]
            notSell = recursion(curri + 1, 0)
            return max(sell, notSell)

        return recursion(0, 1)