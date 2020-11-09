class Solution:
    def reverse(self, x: int) -> int:
        res, ng, x = 0, [1, -1][x < 0], abs(x)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return ng * res * (res < 2 ** 31)
