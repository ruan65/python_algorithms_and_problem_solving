class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        dp = [-1 for _ in range(len(cost) + 1)]
        dp[0] = 0
        dp[1] = cost[0]

        for i in range(2, len(cost) + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    steps = [1, 3, 1, 1, 5]
    print(Solution().minCostClimbingStairs(steps))
