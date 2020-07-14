import sys

from leetcode.greedy_dynamic.big_data import stock_prices

# class Solution:
#     def maxProfit(self, pr: [int]) -> int:
#         if not pr or len(pr) == 1:
#             return 0
#         dp = [0 for _ in range(len(pr))]
#         mn = pr[0]
#         for i in range(1, len(pr)):
#             mn = min(mn, pr[i - 1])
#             dp[i] = max(dp[i-1], pr[i] - mn)
#         return dp[-1]

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        max_profit, min_price = 0, sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    pr_list = [2, 8, 2, 10, 0, 1, 2]
    # print(Solution().maxProfit(pr_list))
    print(Solution().maxProfit(stock_prices))
