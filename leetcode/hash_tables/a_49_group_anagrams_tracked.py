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
    track = set()
    single_track1 = set()
    single_track2 = set()

    for i in range(len(data)):
        if len(data[i]) < 2:
            if data[i] not in single_track1:
                single_track1.add(data[i])
                continue
            if data[i] in single_track1 and (data[i] not in single_track2):
                single_track2.add(data[i])
                res.append([data[i], data[i]])
                continue
        if data[i] in track:
            continue
        track.add(data[i])
        an = [data[i]]
        for j in range(i + 1, len(data)):
            if data[j] in track:
                continue
            if is_anagram(data[i], data[j]):
                an.append(data[j])
                track.add(data[j])
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
    # print(group_anagrams(["bat"]))
    print(group_anagrams(["ant", "ant"]))
    # print(group_anagrams([]))
    # print(group_anagrams(['', '']))
    # print(group_anagrams(['', '', '']))
    # print(group_anagrams(['']))
