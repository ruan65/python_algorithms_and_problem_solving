class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(t) < len(s):
            return False
        if len(s) == len(t):
            return s == t

        poi_s = poi_t = 0

        while poi_t < len(t):
            if s[poi_s] == t[poi_t]:
                poi_s += 1

                if poi_s == len(s):
                    return True
            poi_t += 1
        return False


if __name__ == '__main__':
    print(Solution().isSubsequence("acb",
                                   "ahbgdc"))
