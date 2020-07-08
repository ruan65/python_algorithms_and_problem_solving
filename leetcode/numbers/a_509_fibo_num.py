# class Solution:
#     def fib(self, N: int) -> int:
#         if N == 0:
#             return 0
#         if N == 1:
#             return 1
#
#         return self.fib(N - 1) + self.fib(N - 2)


# def fb(n: int, hm: {int: int}) -> int:
#     if n in hm:
#         return hm[n]
#     result = fb(n - 1, hm) + fb(n - 2, hm)
#     hm[n] = result
#     return result
#
#
# class Solution:
#     def fib(self, N: int) -> int:
#         dc = {0: 0, 1: 1}
#
#         return fb(N, dc)

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        pp = 0
        p = 1
        res = -1

        for i in range(2, N + 1):
            res = pp + p
            pp = p
            p = res
        return res
