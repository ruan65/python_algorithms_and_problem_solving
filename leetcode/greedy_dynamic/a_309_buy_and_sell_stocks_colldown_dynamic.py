"""
dp[len][2] - we have a stock or don't
case 1 -  we have stock on day i: dp[i][1] - max of the below:
    1 I bought it today
        dp[i-2][0] - prices[i]
    2 I'm carry forwarding
        dp[i-1][1]
case 2 -  we have no stock on day i: dp[i][0]
    1 I sold it today
        dp[i-1][1] + prices[i]
    2 I'm carry forwarding (doing nothing)
        dp[i-1][0]
"""


class Solution:
    def maxProfit(self, pr: [int]) -> int:
        if not pr or len(pr) < 2:
            return 0
        n = len(pr)
        if n == 2 and pr[1] > pr[0]:
            return pr[1] - pr[0]
        if n == 2 and pr[1] <= pr[0]:
            return 0
        dp = [[0 for c in range(2)] for r in range(n)]

        dp[0][0] = 0
        dp[0][1] = -pr[0]
        dp[1][0] = max(dp[0][1] + pr[1], dp[0][0])
        dp[1][1] = max(dp[0][1], dp[0][0] - pr[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][1] + pr[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 2][0] - pr[i], dp[i - 1][1])

        print(dp)
        return dp[n - 1][0]

if __name__ == '__main__':
    pr_list = [5,3,12,10,15,15,2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
