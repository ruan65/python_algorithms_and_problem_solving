def are_anagrams(w1, w2) -> bool:
    return sorted(w1) == sorted(w2)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return are_anagrams(s, t)


if __name__ == '__main__':
    print(are_anagrams('hello', 'olleh'))
