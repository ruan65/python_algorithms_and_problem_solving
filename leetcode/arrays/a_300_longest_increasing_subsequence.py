class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        mx = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    mx = max(mx, dp[i])
        return mx