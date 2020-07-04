# class Solution:
#     count = 0
#
#     def rob(self, nums: [int]) -> (int, int):
#         if not nums:
#             return 0
#
#         def rb(i: int) -> int:
#             self.count += 1
#             if i < 0:
#                 return 0
#             return max(rb(i - 1), rb(i - 2) + nums[i])
#
#         return rb(len(nums) - 1), self.count

"""         prev sucks! We should do it with memo
"""


class Solution:
    count = 0

    def rob(self, nums: [int]) -> (int, int):
        if not nums:
            return 0
        memo = [-1 for _ in range(len(nums))]

        def rb(i: int) -> int:
            self.count += 1
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            curr = max(rb(i - 1), rb(i - 2) + nums[i])
            memo[i] = curr
            return curr

        return rb(len(nums) - 1), self.count


if __name__ == '__main__':
    hss = [1, 1, 4, 7, 1, 1, 4]
    # hss = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50,
    #        81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    vl, c = Solution().rob(hss)
    print(vl)
    print(c)
