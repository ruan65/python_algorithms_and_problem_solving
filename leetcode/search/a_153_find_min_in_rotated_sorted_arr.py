# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.

# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

# find pivot index
# take el by pivot


# def _find_pivot_of_arr(arr: [int], s, e) -> int:
#     m = s + (e - s) // 2
#     if len(arr) == 1 or arr[0] < arr[e]:
#         return 0
#     if arr[m] < arr[m - 1]:
#         return m
#     if arr[m + 1] < arr[m]:
#         return m + 1
#     if arr[m] > arr[0]:
#         s = m + 1
#     else:
#         e = m
#     return _find_pivot_of_arr(arr, s, e)
#
#
# def find_pivot(arr: [int]) -> int:
#     s = 0
#     e = len(arr) - 1
#     return _find_pivot_of_arr(arr, s, e)
#
#
# class Solution:
#     def findMin(self, nums: [int]) -> int:
#         pivot = find_pivot(nums)
#         return nums[pivot]

class Solution:
    def findMin(self, nums: [int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            m = (low + high) // 2
            if nums[m] < nums[high]:
                high = m
            elif nums[m] > nums[high]:
                low = m + 1
        return nums[low]


if __name__ == '__main__':
    print(f'min: {Solution().findMin([4, 5, 1, 2, 3])}')
