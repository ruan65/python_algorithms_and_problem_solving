# def str_to_dict(text: str) -> {str: int}:
#     res = {}
#     for c in text:
#         if c not in res:
#             res[c] = 1
#         else:
#             res[c] += 1
#     return res
#
#
# def are_anagrams(w1, w2) -> bool:
#     return str_to_dict(w1) == str_to_dict(w2)
import collections


def are_anagrams(w1, w2) -> bool:
    return sorted(w1) == sorted(w2)


#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return are_anagrams(s, t)

# def isAnagram(self, s, t):
#     return collections.Counter(s) == collections.Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track = collections.defaultdict(int)
        for c in s:
            track[c] += 1
        for ch in t:
            track[ch] -= 1
        return all(n == 0 for n in track.values())
