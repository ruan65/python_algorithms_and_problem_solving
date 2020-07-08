class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1
        mx = amount + 1
        dp = [amount + 1 for _ in range(mx)]
        dp[0] = 0
        coins.sort()

        for a in range(1, mx):
            tmp = [mx]
            for c in coins:
                if a - c < 0:
                    break
                tmp.append(dp[a - c])
            dp[a] = min(tmp) + 1

        return dp[amount] if dp[amount] != mx else -1


print(Solution().coinChange([1, 2, 5], 19))
