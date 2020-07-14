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
# def incr_or_add(el: str, dct: {str: int}):
#     if el in dct:
#         dct[el] += 1
#     else:
#         dct[el] = 1
#
#
# def decr_or_remove(el: str, dct: {str: int}):
#     if el in dct:
#         if dct[el] > 1:
#             dct[el] -= 1
#         else:
#             del dct[el]
#
#
# def find_all_anagrams(s: str, w: str) -> [int]:
#     result = []
#     if not s or len(s) < len(w):
#         return result
#     start = 0
#     p_count: {str: int} = str_to_dict(w)
#     s_count: {str: int} = str_to_dict(s[0:len(w) - 1])
#
#     for end in range(len(w) - 1, len(s)):
#         incr_or_add(s[end], s_count)
#         if s_count == p_count:
#             result.append(start)
#         decr_or_remove(s[start], s_count)
#         start += 1
#     return result
#
#
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> [int]:
#         return find_all_anagrams(s, p)


def str_to_dic(s: str) -> {str: int}:
    res = {}
    for c in s:
        res[c] = res.get(c, 0) + 1
    return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        if not s or len(s) < len(p):
            return []
        res = []
        pattern = str_to_dic(p)
        match = str_to_dic(s[0:len(p) - 1])
        start = 0
        for end in range(len(p) - 1, len(s)):
            match[s[end]] = match.get(s[end], 0) + 1
            if pattern == match:
                res.append(start)

            if s[start] in match:
                if match[s[start]] == 1:
                    match.pop(s[start], None)
                else:
                    match[s[start]] -= 1
            start += 1
        return res
