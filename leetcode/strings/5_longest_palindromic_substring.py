class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if s == s[::-1]:
            return s

        def pal_exp(k, j) -> (int, int, int):
            while k > 0 and j < len(s) - 1 and s[k] == s[j]:
                if s[k - 1] == s[j + 1]:
                    k -= 1
                    j += 1
                else:
                    break
            return j - k, k, j

        ms = me = mlen = 0

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                ln, cs, ce = pal_exp(i, i + 1)
                if ln > mlen:
                    mlen = ln
                    ms = cs
                    me = ce
            if i > 0 and s[i - 1] == s[i + 1]:
                ln, cs, ce = pal_exp(i, i)
                if ln > mlen:
                    mlen = ln
                    ms = cs
                    me = ce

        return s[ms: me + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome("xsooos"))
