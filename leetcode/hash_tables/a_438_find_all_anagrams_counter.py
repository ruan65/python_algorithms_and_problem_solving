from collections import Counter


def find_all_anagrams(s: str, w: str) -> [int]:
    result = []
    if not s or len(s) < len(w):
        return result
    start = 0
    p_count: Counter = Counter(w)
    s_count: Counter = Counter(s[start:len(w) - 1])

    for end in range(len(w) - 1, len(s)):
        s_count[s[end]] += 1
        if s_count == p_count:
            result.append(start)
        s_count[s[start]] -= 1
        if s_count[s[start]] == 0:
            del s_count[s[start]]
        start += 1
    return result


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        return find_all_anagrams(s, p)


if __name__ == '__main__':
    print(find_all_anagrams("cbaebabacd", "abc"))
