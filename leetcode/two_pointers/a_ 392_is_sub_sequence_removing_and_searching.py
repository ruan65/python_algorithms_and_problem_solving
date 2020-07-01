class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        cmp = ''
        for c in t:
            if c in s:
                cmp += c
        if len(cmp) < len(s):
            return False
        while s:
            ind = cmp.find(s[0])
            if ind == -1:
                return False
            s = s[1:]
            cmp = cmp[ind:]

        return True


if __name__ == '__main__':
    print(Solution().isSubsequence("aaaaaa",
                                   "bbaaaa"))
