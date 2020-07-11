# def group_anagrams(data: [str]) -> [[str]]:
#     track = {}
#     for w in data:
#         srt = str(sorted(w))
#         if srt not in track:
#             track[srt] = []
#         track[srt].append(w)
#     return list(track.values())
#
#
# class Solution:
#     def groupAnagrams(self, strs: [str]) -> [[str]]:
#         return group_anagrams(strs)

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        dct = {}
        for w in strs:
            srt = str(sorted(w))
            if srt in dct:
                dct[srt].append(w)
            else:
                dct[srt] = [w]
        return dct.values()


if __name__ == '__main__':
    pass
    # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(group_anagrams(["bat"]))
    # print(group_anagrams(ana_big))
    # print(group_anagrams([]))
    # print(group_anagrams(['', '']))
    # print(group_anagrams(['', '', '']))
    # print(group_anagrams(['']))
