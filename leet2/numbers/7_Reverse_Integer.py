class Solution:
    def reverse(self, x: int) -> int:
        res, ng, x = 0, -1 if x < 0 else 1, abs(x)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return ng * res if res < 2 ** 31 else 0
