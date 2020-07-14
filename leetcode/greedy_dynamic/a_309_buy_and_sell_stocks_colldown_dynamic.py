class Solution:
    def maxProfit(self, pr: [int]) -> int:
        if not pr or len(pr) < 2:
            return 0

        dp = [[0 for _ in range(len(pr))] for _ in [0,1]]

        dp[0][0] = 0
        dp[1][0] = -pr[0]
        dp[0][1] = max(dp[0][0], dp[1][0] + pr[1])
        dp[1][1] = max(dp[1][0], dp[0][0] - pr[1])

        for i in range(2, len(pr)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + pr[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-2] - pr[i])

        return dp[0][-1]

if __name__ == '__main__':
    pr_list = [5,3,12,10,15,15,2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
