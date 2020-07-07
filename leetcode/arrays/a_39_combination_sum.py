class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        def bt(ind: int, nms: [int], ct: int):
            if ct == 0:
                res.append(list(nms))
                return
            elif ct < 0:
                return
            nm = candidates[ind]
            nms.append(nm)
            bt(ind, nms, ct - nm)
            nms.pop()
            if ind < len(candidates) - 1:
                bt(ind + 1, nms, ct)

        res = []
        if not candidates:
            return res
        bt(0, [], target)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 5], 9))
