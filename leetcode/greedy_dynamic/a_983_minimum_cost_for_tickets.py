class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        pr1, pr7, pr30 = costs[0], costs[1], costs[2]
        last_day = days[-1]
        dp = [2**31 for _ in range(last_day + 1)]
        travel = [False for _ in range(last_day + 1)]
        dp[0] = 0
        for d in days:
            travel[d] = True
        for i in range(1, len(dp)):
            if not travel[i]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + pr1, dp[max(i - 7, 0)] +
                            pr7, dp[max(i - 30, 0)] + pr30)
        return dp[last_day]


ds = [1, 4, 6, 7, 8, 20]
price = [2, 7, 15]
print(Solution().mincostTickets(ds, price))
