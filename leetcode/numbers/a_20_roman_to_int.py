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
        
# class Solution:
#     def romanToInt(self, s):
#         map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         num, pre = 0, 1000
#         for n in [map[j] for j in s]:
#             num, pre = num + n - 2 * pre if n > pre else num + n, n
#         return num

if __name__ == '__main__':
    print(Solution().romanToInt('VIV'))

