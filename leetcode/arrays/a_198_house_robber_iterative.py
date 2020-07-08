# class Solution:
#
#     def rob(self, nums: [int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         memo = [-1 for _ in range(len(nums))]
#
#         memo[0] = nums[0]
#         memo[1] = max(nums[0], nums[1])
#
#         for i in range(2, len(nums)):
#             memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
#
#         return memo[len(nums) - 1]
"""
    similar but with 2 vars (less memory)
"""

class Solution:

    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        slow = nums[0]
        fast = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = fast
            fast = max(fast,  slow + nums[i])
            slow = curr

        return fast


if __name__ == '__main__':
    # hss = [1, 1, 4, 7, 1, 1, 4]
    hss = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50,
           81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    vl = Solution().rob(hss)
    print(vl)
