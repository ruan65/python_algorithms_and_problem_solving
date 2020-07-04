def rb(arr: [int]) -> int:
    if len(arr) == 1:
        return arr[0]
    slow = arr[0]
    fast = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        tmp = fast
        fast = max(fast, slow + arr[i])
        slow = tmp
    return fast


class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rb(nums[1:]), rb(nums[:-1]))