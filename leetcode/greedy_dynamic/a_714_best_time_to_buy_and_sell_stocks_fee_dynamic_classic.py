"""
every day we can have a stock or not
case 0: not have (max of below)
    var 1: sold today
        dp[i][0] = dp[i-1][1] + pr[i] - fee
    var 2: carrying (do nothing today)
        dp[i][0] = dp[i-1][0]
case 1: have (max of below)
    var 1: bought today
        dp[i][1] = dp[i-1][0] - pr[i]
    var 2: carrying
        dp[i][1] = dp[i-1][1]

    return dp[n][0]
"""
from leetcode.greedy_dynamic.big_data import stock_prices


class Solution:
    def maxProfit(self, pr: [int], fee: int) -> int:
        if not pr or len(pr) < 2:
            return 0
        n = len(pr)

        dp = [[0 for r in range(2)] for c in range(n)]

        dp[0][0] = 0
        dp[0][1] = -pr[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + pr[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - pr[i])
        print(dp)

        return dp[n - 1][0]


if __name__ == '__main__':
    pr_list = [1, 3, 7, 5, 10, 3]
    print(Solution().maxProfit(pr_list, 3))
    # print(Solution().maxProfit(stock_prices, 0))
