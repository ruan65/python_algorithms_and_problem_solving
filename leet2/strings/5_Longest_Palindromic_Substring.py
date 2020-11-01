class Solution:
    @staticmethod
    def helper(s, b, e):
        res = s[0]
        while b >= 0 and e < len(s) and s[b] == s[e]:
            if len(res) < len(s[b:e + 1]):
                res = s[b:e + 1]
                b -= 1
                e += 1
        return res

    def longestPalindrome(self, s: str) -> str:
        lp = s[0]
        for i in range(1, len(s)):
            b, e = i - 1, i + 1
            curr = self.helper(s, b, e)
            if len(curr) > len(lp):
                lp = curr
            b, e = i - 1, i
            curr = self.helper(s, b, e)
            if len(curr) > len(lp):
                lp = curr
        return lp
