# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# def find_target_sum_indexes(arr: [int], target: int) -> [int]:
#     ht = {}
#     for i in range(len(arr)):
#         if target - arr[i] in ht:
#             return [i, ht[target - arr[i]]]
#         ht[arr[i]] = i
#     return []
#
#
# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         return find_target_sum_indexes(nums, target)

# two-pointer
# def twoSum(self, nums, target):
#     nums = enumerate(nums)
#     nums = sorted(nums, key=lambda x:x[1])
#     l, r = 0, len(nums)-1
#     while l < r:
#         if nums[l][1]+nums[r][1] == target:
#             return sorted([nums[l][0]+1, nums[r][0]+1])
#         elif nums[l][1]+nums[r][1] < target:
#             l += 1
#         else:
#             r -= 1

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hm: {int: int} = {}
        for i, n in enumerate(nums):
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
        return []


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    # print(find_target_sum_indexes([2, 7, 11, 15], 9))
