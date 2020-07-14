class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, 'O': 0}
        if not s:
            return 0
        if len(s) == 1:
            return m[s]
        s += 'O'
        res = 0
        for i in range(1, len(s)):
            if m[s[i - 1]] < m[s[i]]:

                res -= m[s[i - 1]]
            else:
                res += m[s[i - 1]]
        return res
