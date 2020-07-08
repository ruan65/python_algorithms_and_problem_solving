class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        sl = mx = 0
        fs = 1
        cur = s[0]
        tr = k
        calc = True
        while sl < len(s) and fs < len(s):
            if calc:
                if tr > 0 and s[fs] != cur:
                    fs += 1
                    tr -= 1
                    mx = max(mx, fs - sl)
                elif s[fs] == cur:
                    fs += 1
                    mx = max(mx, fs - sl)
                else:
                    calc = False
            else:
                if s[sl] == cur:
                    sl += 1
                else:
                    cur = s[sl]
                    calc = True
                    tr = k
        return mx
if __name__ == '__main__':
    txt = 'ANNAZZZ'
    print(Solution().characterReplacement(txt, 2))
