class Solution:
    def letterCasePermutation(self, S: str) -> [str]:

        def back_track(sbs='', i=0):
            if len(sbs) == len(S):
                res.append(sbs)
            else:
                if S[i].isalpha():
                    back_track(sbs + S[i].lower(), i + 1)
                    back_track(sbs + S[i].upper(), i + 1)
                else:
                    back_track(sbs + S[i], i + 1)

        res = []
        back_track()
        return res

# class Solution:
#     def letterCasePermutation(self, S):
#         res = [S]
#         for i, c in enumerate(S):
#             if c.isalpha():
#                 res.extend([s[:i] + s[i].swapcase() + s[i + 1:] for s in res])
#         return res

# from collections import deque
# class Solution:
#     def letterCasePermutation(self, S):
#         res = [""]
#         queue = deque(S)
#
#         while queue:
#             nxt = queue.popleft()
#             if nxt.isalpha():
#                 res = [sub + nxt for sub in res] + [sub + nxt.swapcase() for sub in res]
#             else:
#                 res = [sub + nxt for sub in res]
#         return res

if __name__ == '__main__':
    inp = 'a1b2'
    print(Solution().letterCasePermutation(inp))
