"""
every day we can have a stock or not
case 0: not have (max of below)
    var 1: sold today
        dp[0][i] = dp[1][i-1] + pr[i] - fee
    var 2: carrying (do nothing today)
        dp[0][i] = dp[0][i-1]
case 1: have (max of below)
    var 1: bought today
        dp[1][i] = dp[0][i-1] - pr[i]
    var 2: carrying
        dp[1][i] = dp[1][i-1]

    return dp[n][0]
"""


class Solution:
    def maxProfit(self, pr: [int], fee: int) -> int:
        if not pr or len(pr) < 2:
            return 0
        n = len(pr)

        dp = [[0 for c in range(n)] for r in range(2)]

        dp[0][0] = 0
        dp[1][0] = -pr[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + pr[i] - fee)
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - pr[i])

        for r in dp:
            print(r)

        return dp[0][n - 1]


if __name__ == '__main__':
    pr_list = [1, 3, 7, 5, 10, 3]
    print(Solution().maxProfit(pr_list, 3))
    # print(Solution().maxProfit(stock_prices, 0))
