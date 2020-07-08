class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        for t in range(1, target + 1):  # dp[t] saves all combinations have t sum
            for i in candidates:
                if i > t:
                    break  # from now on, all sum > t, break out
                if i == t:
                    dp[t].append([i])
                    break  # the element value equals to current target t
                # to ensure no duplicate, the later coming item should be strictly greater
                # than previous ones, make the result a asc sequence.
                dp[t].extend(path + [i] for path in dp[t - i] if i >= path[-1])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().combinationSum([3, 2, 5], 9))
