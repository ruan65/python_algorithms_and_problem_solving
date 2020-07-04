class Solution:
    count = 0

    def rob(self, nums: [int]) -> (int, int):
        if not nums:
            return 0
        dp = [[-1 for _ in range(len(nums))] for __ in range(2)]

        def rob_or_not(i: int, can: bool, v: int) -> int:
            self.count += 1
            if i < 0:
                return v
            if not can:
                return rob_or_not(i - 1, True, v)
            opt1 = rob_or_not(i - 1, False, v + nums[i])
            opt2 = rob_or_not(i - 1, True, v)
            return max(opt2, opt1)

        return rob_or_not(len(nums) - 1, True, 0), self.count


if __name__ == '__main__':
    # hss = [1, 1, 4, 7, 1, 1, 4]
    hss = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50,
           81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    # n = len(hss)
    # print(n)
    # print(n * n)
    # print(n * n * n)
    vl, c = Solution().rob(hss)
    print(vl)
    print(c)
