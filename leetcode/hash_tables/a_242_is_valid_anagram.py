def str_to_dict(text: str) -> {str: int}:
    res = {}
    for c in text:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1
    return res


def are_anagrams(w1, w2) -> bool:
    return str_to_dict(w1) == str_to_dict(w2)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return are_anagrams(s, t)


if __name__ == '__main__':
    print(str_to_dict('hello'))
