class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        curr = mx = nums[0]
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            mx = max(mx, curr)
        return mx


if __name__ == '__main__':
    # nms = [1, 2, 3, -1, 1, 10]
    nms = [1, 2]
    print(Solution().maxSubArray(nms))
