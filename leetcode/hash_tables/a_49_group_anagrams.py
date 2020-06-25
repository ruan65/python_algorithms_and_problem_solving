# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
from leetcode.hash_tables.big_data import ana_large, ana_big


def is_anagram(w1, w2):
    return string_to_dict(w1) == string_to_dict(w2)


def string_to_dict(text):
    result = {}
    for c in text:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


def group_anagrams(data: [str]) -> [[str]]:
    res: [[str]] = []
    single_track1 = set()
    single_track2 = set()

    for w in data:
        if w not in single_track1:
            single_track1.add(w)
            continue
        if w in single_track1 and w not in single_track2:
            single_track2.add(w)
            continue

    unique = list(single_track2)
    for i in range(len(unique)):
        an = [unique[i]]
        for j in range(1, len(unique)):
            if is_anagram(unique[i], unique[j]):
                an.append(unique[j])
        if len(an) == 2:
            res.append(an)
    for sd in single_track1:
        if sd not in single_track2:
            res.append([sd])
    return res


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        return group_anagrams(strs)


if __name__ == '__main__':
    # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams(["bat"]))
    # print(group_anagrams(ana_big))
    # print(group_anagrams([]))
    # print(group_anagrams(['', '']))
    # print(group_anagrams(['', '', '']))
    # print(group_anagrams(['']))
