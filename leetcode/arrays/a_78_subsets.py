# class Solution:
#     def subsets(self, nums: [int]) -> [[int]]:
#
#         def bt(start: int, curr: []):
#             res.append(list(curr))
#             for i in range(start, len(nums)):
#                 if nums[i] not in curr:
#                     curr.append(nums[i])
#                 bt(i + 1, curr)
#                 curr.pop()
#
#         res = []
#         bt(0, [])
#         return res

class Solution:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            res += [subset + [n] for subset in res]
        return res


if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))