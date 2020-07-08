# class Solution:
#     def reverse(self, x: int) -> int:
#         negative = False
#         st = str(x)
#         if st[0] == '-':
#             negative = True
#             st = st[1:]
#         st = st[::-1]
#
#         num = int(st)
#         if negative:
#             num = -num
#         if num > pow(2, 31) - 1 or num < -pow(2, 31):
#             return 0
#
#         return num


class Solution:
    def reverse(self, x: int) -> int:
        num = [1, -1][x < 0] * int(str(abs(x))[::-1])
        return num if -pow(2, 31) < num < pow(2, 31) - 1 else 0
