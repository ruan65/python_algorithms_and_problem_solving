class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        hm = {}
        for w in strs:
            srt = str(sorted(w))
            if srt in hm:
                hm[srt].append(w)
            else:
                hm[srt] = [w]

        return hm.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
