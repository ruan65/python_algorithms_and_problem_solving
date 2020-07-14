"""
    do not have stock dp[0][i] = max of
        1) sold  dp[1][i-1] + pr[i]
        2) carry dp[0][i-1]
    have stock dp[1][i] = max of
        1) bought dp[0][i-1] - pr[i]
        2) carry  dp[1][i-1]
"""
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

class Solution:
    def maxProfit(self, pr: [int]) -> int:
        if not pr or len(pr) < 2:
            return 0
        dp = [[0 for _ in range(len(pr))] for _ in [0,1]]

        dp[1][0] = -pr[0]

        for i in range(1, len(pr)):
            # do not have (sold or carry)
            dp[0][i] = max(dp[0][i-1], pr[i] + dp[1][i-1])
            # have (bought or carry)
            dp[1][i] = max(dp[0][i-1] - pr[i], dp[1][i-1])

        return dp[0][-1]


if __name__ == '__main__':
    pr_list = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
