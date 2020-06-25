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


def find_all_anagrams(string: str, w: str) -> [int]:
    if string == w:
        return 0
    res = []
    for i in range(len(string) - len(w) + 1):
        w2 = string[i:i + len(w)]
        if are_anagrams(w, w2):
            res.append(i)
    return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        return find_all_anagrams(s, p)


if __name__ == '__main__':
    print(find_all_anagrams("qqqqqqqqq", "qqqqqqqqq"))
