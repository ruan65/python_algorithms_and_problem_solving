class Solution:
    hm: {(int, int): int} = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if (m, n) in self.hm:
            return self.hm[(m, n)]
        result = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self.hm[(m, n)] = result
        return result


if __name__ == '__main__':
    print(Solution().uniquePaths(6, 6))
