count = 0


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         global count
#         if not s:
#             return 0
#
#         track = set()
#         sl, fs = 0, 0
#         res = 0
#         while fs < len(s):
#             count += 1
#             if s[fs] not in track:
#                 track.add(s[fs])
#                 fs += 1
#                 if res < fs - sl:
#                     res = fs - sl
#             else:
#                 track.clear()
#                 sl += 1
#                 fs = sl
#
#         return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        track = set()
        sl = fs = max_len = 0

        while sl < len(s) and fs < len(s):
            if s[fs] not in track:
                track.add(s[fs])
                fs += 1
                max_len = max(max_len, fs - sl)
            else:
                track.remove(s[sl])
                sl += 1
        return max_len

if __name__ == '__main__':
    # sss = "aqwertyuiopsdfghjkllkjaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" * 100
    sss = "kabazxa"
    print(f'solution: {Solution().lengthOfLongestSubstring(sss)}')
    print(f'len={len(sss)}')
    print(f'count={count}')
