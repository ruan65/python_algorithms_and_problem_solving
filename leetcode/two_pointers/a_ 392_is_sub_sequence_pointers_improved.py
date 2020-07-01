class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(t) < len(s):
            return False
        if len(s) == len(t):
            return s == t

        poi_s = poi_t = 0

        while poi_s < len(s) and poi_t < len(t):

            ind = t[poi_t:].find(s[poi_s])
            if ind == -1:
                return False
            poi_s += 1
            poi_t = poi_t + ind + 1
            if len(t) - poi_t < len(s) - poi_s:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isSubsequence("ac",
                                   "ahbgdc"))
