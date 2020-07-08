def str_to_dict(text: str) -> {str: int}:
    res = {}
    for c in text:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1
    return res


def incr_or_add(el: str, dct: {str: int}):
    if el in dct:
        dct[el] += 1
    else:
        dct[el] = 1


def decr_or_remove(el: str, dct: {str: int}):
    if el in dct:
        if dct[el] > 1:
            dct[el] -= 1
        else:
            del dct[el]


def find_all_anagrams(s: str, w: str) -> [int]:
    result = []
    if not s or len(s) < len(w):
        return result
    start = 0
    p_count: {str: int} = str_to_dict(w)
    s_count: {str: int} = str_to_dict(s[0:len(w) - 1])

    for end in range(len(w) - 1, len(s)):
        incr_or_add(s[end], s_count)
        if s_count == p_count:
            result.append(start)
        decr_or_remove(s[start], s_count)
        start += 1
    return result


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        return find_all_anagrams(s, p)


if __name__ == '__main__':
    print(find_all_anagrams("abacabd", "ab"))
