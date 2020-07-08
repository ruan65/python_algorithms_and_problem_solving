from collections import defaultdict


def str_to_dict(s: str) -> {str: int}:
    dct = defaultdict(int)
    for c in s:
        dct[c] += 1
    return dct


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         matcher = str_to_dict(s1)
#         print(matcher)
#
#         for i in range(len(s2) - len(s1) + 1):
#             e = i + len(s1) - 1
#             sbs = s2[i:e + 1]
#             print(sbs)
#             if matcher == str_to_dict(sbs):
#                 return True
#         return False

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        matcher = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            e = i + len(s1) - 1
            sbs = s2[i:e + 1]
            print(sbs)
            if matcher == Counter(sbs):
                return True
        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#
#         k = len(s1)
#         from collections import Counter
#         d1 = Counter(s1)
#
#         # initial window
#         window = s2[:k]
#         d2 = Counter(window)
#
#         print(d2)
#
#         # check the intial window
#         if d1 == d2:
#             return True
#
#         for i in range(len(s2) - k):
#
#             # SLIDE THE WINDOW
#             # 1 - remove s2[i]
#             if d2[s2[i]] == 1:
#                 del d2[s2[i]]
#             elif d2[s2[i]] > 1:
#                 d2[s2[i]] -= 1
#
#             # 2- add s2[i+k]
#             if s2[i + k] in d2:
#                 d2[s2[i + k]] += 1
#             else:
#                 d2[s2[i + k]] = 1
#
#             # check after sliding
#             if d1 == d2:
#                 return True
#
#         return False


if __name__ == '__main__':
    ss = 'ab'
    inp = 'ccbadd'
    print(Solution().checkInclusion(ss, inp))
