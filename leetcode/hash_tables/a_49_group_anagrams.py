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


def group_anagrams(data: [str]) -> [[str]]:
    track = {}
    for w in data:
        srt = str(sorted(w))
        if srt not in track:
            track[srt] = []
        track[srt].append(w)
    return list(track.values())


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        return group_anagrams(strs)


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams(["bat"]))
    # print(group_anagrams(ana_big))
    # print(group_anagrams([]))
    # print(group_anagrams(['', '']))
    # print(group_anagrams(['', '', '']))
    # print(group_anagrams(['']))
