class Solution:
    def maxProduct(self, nums: [int]) -> int:

        mx = mn = ans = nums[0]

        for n in nums[1:]:
            cmx = max(mx * n, mn * n, n)
            mn = min(mx * n, mn * n, n)
            mx = cmx
            ans = max(ans, cmx)

        return ans


if __name__ == '__main__':
    ar = [-4, -3, -2]
    print(Solution().maxProduct(ar))
