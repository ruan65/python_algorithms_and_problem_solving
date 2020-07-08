# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
#         return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
#

def tribo(n: int, hm: {int: int}) -> int:
    if n in hm:
        return hm[n]
    res = tribo(n - 1, hm) + tribo(n - 2, hm) + tribo(n - 3, hm)
    hm[n] = res
    return res


class Solution:
    def tribonacci(self, n: int) -> int:
        return tribo(n, {0: 0, 1: 1, 2: 1})
