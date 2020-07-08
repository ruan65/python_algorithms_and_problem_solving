# class Solution:
#     hm: {(int, int): int} = {}
#
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 1 or n == 1:
#             return 1
#         if (m, n) in self.hm:
#             return self.hm[(m, n)]
#         result = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
#         self.hm[(m, n)] = result
#         return result


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp: [[int]] = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(6, 6))
