def find_all_anagrams(string: str, w: str) -> [int]:
    if string == w:
        return [0]
    srt = sorted(w)
    if len(string) == len(w):
        if srt == sorted(string):
            return [0]
        else:
            return []
    res = []
    for i in range(len(string) - len(w) + 1):
        w2 = string[i:i + len(w)]
        if srt == sorted(w2):
            res.append(i)
    return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        return find_all_anagrams(s, p)


if __name__ == '__main__':
    print(find_all_anagrams("qqqqqqqqq1", "qqqq"))
