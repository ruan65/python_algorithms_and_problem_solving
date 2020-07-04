"""
    do not have stock dp[0][i] = max of
        1) sold  dp[1][i-1] + pr[i]
        2) carry dp[0][i-1]
    have stock dp[1][i] = max of
        1) bought dp[0][i-1] - pr[i]
        2) carry  dp[1][i-1]
"""


class Solution:
    def maxProfit(self, pr: [int]) -> int:
        if not pr or len(pr) < 2:
            return 0
        n = len(pr)
        dp = [[0 for c in range(n)] for r in range(2)]

        dp[0][0] = 0
        dp[1][0] = -pr[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + pr[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - pr[i])

        for r in dp:
            print(r)
        return dp[0][n - 1]


if __name__ == '__main__':
    pr_list = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
