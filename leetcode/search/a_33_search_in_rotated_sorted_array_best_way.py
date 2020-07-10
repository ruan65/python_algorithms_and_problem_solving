class Solution:
    def search(self, nums: [int], t: int) -> int:
        if not nums:
            return -1
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if t == nums[m]:
                return m
            if nums[s] <= nums[m]:
                if nums[s] <= t < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[m] < t <= nums[e]:
                    s = m + 1
                else:
                    e = m
        return -1


if __name__ == '__main__':
    print(Solution().search([5, 6, 7, 8, 16, -100, -20, 0, 1, 2, 3, 45, 67, 89], 0))
