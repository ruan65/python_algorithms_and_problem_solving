# class Solution:
#     def combinationSum(self, candidates: [int], target: int) -> [[int]]:
#         def bt(ind: int, nms: [int], ct: int):
#             if ct == 0:
#                 res.append(list(nms))
#                 return
#             elif ct < 0:
#                 return
#             nm = candidates[ind]
#             nms.append(nm)
#             bt(ind, nms, ct - nm)
#             nms.pop()
#             if ind < len(candidates) - 1:
#                 bt(ind + 1, nms, ct)
#
#         res = []
#         if not candidates:
#             return res
#         bt(0, [], target)
#         return res

# class Solution:
#     def combinationSum(self, candidates, target):
#         def dfs(nums, trg, index, path):
#             if trg < 0:
#                 return  # backtracking
#             if trg == 0:
#                 res.append(path)
#                 return
#             for i in range(index, len(nums)):
#                 dfs(nums, trg - nums[i], i, path + [nums[i]])
#         res = []
#         dfs(candidates, target, 0, [])
#         return res

class Solution:
    def combinationSum(self, candidates, target):
        def dfs(trg, index, path):
            if trg < 0:
                return  # backtracking
            if trg == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(trg - candidates[i], i, path + [candidates[i]])

        res = []
        dfs(target, 0, [])
        return res




if __name__ == '__main__':
    print(Solution().combinationSum([3, 2, 5], 9))
