class Solution:

    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp: [int] = [0 for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


if __name__ == '__main__':
    # hss = [1, 1, 4, 7, 1, 1, 4, 1]
    hss = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50,
           81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]

    vl = Solution().rob(hss)
    print(vl)
