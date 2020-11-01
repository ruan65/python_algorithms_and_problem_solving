# def is_unique(s):
#     st = set(s)
#     return len(st) == len(s)
#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         f, e, mx = 0, 0, 0
#         while e < len(s):
#             if is_unique(s[f:e + 1]):
#                 mx = max(mx, e - f + 1)
#                 e += 1
#             else:
#                 f += 1
#         return mx

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t, r, mx, st = 0, 0, 0, set()
        while r < len(s):
            if s[r] not in st:
                mx = max(mx, r - t + 1)
                st.add(s[r])
                r += 1
            else:
                st.remove(s[t])
                t += 1
        return mx
