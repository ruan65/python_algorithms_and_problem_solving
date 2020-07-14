class Solution:
    def maxProfit(self, pr: [int], fee: int) -> int:
        if not pr or len(pr) < 2:
            return 0

        dp = [[0 for _ in range(len(pr))] for _ in [0,1]]

        dp[1][0] = -pr[0]

        for i in range(1, len(pr)):
            # do not have (sold or carry)
            dp[0][i] = max(dp[1][i-1] + pr[i] - fee, dp[0][i-1])
            # have (bought or carry)
            dp[1][i] = max(dp[0][i-1] - pr[i], dp[1][i-1])
        return max(dp[0][-1], 0)


if __name__ == '__main__':
    pr_list = [1, 3, 7, 5, 10, 3]
    print(Solution().maxProfit(pr_list, 3))
    # print(Solution().maxProfit(stock_prices, 0))
