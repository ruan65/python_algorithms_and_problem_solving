class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [1000] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            print(f'am: {i}')
            temp = [1000]
            for c in coins:
                if i - c < 0:
                    break
                temp.append(dp[i - c])
            print(temp)
            dp[i] = min(temp) + 1
            print(dp)

        return dp[amount] if dp[amount] != 1000 else -1


print(Solution().coinChange([2, 3], 5))
