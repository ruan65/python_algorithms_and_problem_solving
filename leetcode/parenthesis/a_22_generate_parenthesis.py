# class Solution:
#     def generateParenthesis(self, n: int) -> [str]:
#         res = []
#
#         def generate(sq, o, c):
#             if len(sq) == 2 * n:
#                 res.append(sq)
#                 return
#
#             if o < n:
#                 generate(sq + '(', o + 1, c)
#
#             if c < o:
#                 generate(sq + ')', o, c + 1)
#
#         generate('', 0, 0)
#     return res


# class Solution:
#     def generateParenthesis(self, n):
#         res=[]
#         def generate(p, l, r):
#             if l:
#                 generate(p + '(',  l - 1, r)
#             if r > l:
#                 generate(p + ')', l, r - 1)
#             if not r:
#                 res.append(p)
#         generate('', n, n)
#         return res


class Solution:
    def generateParenthesis(self, n):
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l < r or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x + "(", l + 1, r))
            s.append((x + ")", l, r + 1))
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(2))
