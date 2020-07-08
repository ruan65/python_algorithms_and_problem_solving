# class Solution:
#     def permute(self, nums: [int]) -> [[int]]:
#         def bt(curr: [int], ind: int):
#             if ind == len(nums):
#                 res.append(curr)
#             for i in range(ind, len(nums)):
#                 curr[i], curr[ind] = curr[ind], curr[i]
#                 bt(list(curr), ind + 1)
#
#         res = []
#         bt(nums, 0)
#         return res


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def bt(curr: [int], start: int, end: int):
            if start == end:
                res.append(curr)
            for i in range(start, end + 1):
                curr[i], curr[start] = curr[start], curr[i]
                bt(list(curr), start + 1, end)
                curr[start], curr[i] = curr[i], curr[start]

        res = []
        bt(nums, 0, len(nums) - 1)
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2]))
