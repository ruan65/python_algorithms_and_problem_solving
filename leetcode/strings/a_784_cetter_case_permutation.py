class Solution:
    def letterCasePermutation(self, S: str) -> [str]:

        def back_track(sbs='', i=0):
            if len(sbs) == len(S):
                res.append(sbs)
            else:
                if S[i].isalpha():
                    back_track(sbs + S[i].swapcase(), i + 1)
                back_track(sbs + S[i], i + 1)

        res = []
        back_track()
        return res


if __name__ == '__main__':
    inp = 'a1b2'
    print(Solution().letterCasePermutation(inp))
