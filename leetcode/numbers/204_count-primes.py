class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        mask = [1 for _ in range(n)]

        for i in range(2, n):
            if mask[i]:
                res += 1
                for j in range(i, n, i):
                    mask[j] = 0
        return res

if __name__ == '__main__':
    print(Solution().countPrimes(10))

