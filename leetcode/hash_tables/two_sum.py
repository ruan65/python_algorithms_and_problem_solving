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


def find_target_sum_indexes(arr: [int], target: int) -> [int]:
    ht = {}
    for i in range(len(arr)):
        if target - arr[i] in ht:
            return [i, ht[target - arr[i]]]
        ht[arr[i]] = i
    return []


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        return find_target_sum_indexes(nums, target)


if __name__ == '__main__':
    print(find_target_sum_indexes([2, 7, 11, 15], 9))
