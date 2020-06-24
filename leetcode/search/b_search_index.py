def b_search_index(nums: [int], target: int, s=0) -> int:
    if not nums:
        return -1
    m = len(nums) // 2
    if nums[m] == target:
        return m + s
    elif target > nums[m]:
        return b_search_index(nums[m + 1:], target, s=s + m + 1)
    else:
        return b_search_index(nums[:m], target, s=s)


class Solution:
    def search(self, nums: [int], target: int) -> int:
        return b_search_index(nums, target)
