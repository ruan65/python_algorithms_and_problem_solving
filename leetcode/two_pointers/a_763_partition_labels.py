class Solution:
    def partitionLabels(self, S: str) -> [int]:
        if len(S) == 1:
            return [1]
        last_ind = {ch: S.rindex(ch) for ch in S}

        res = []
        s = e = 0
        for i in range(len(S)):
            e = max(e, last_ind[S[i]])
            if e == i:
                res.append(e - s + 1)
                s = i + 1
        return res


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
    # [9, 7, 8]
