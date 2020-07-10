class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if not nums:
            return False

        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2
            if target == nums[m]:
                return True
            while nums[s] == nums[m] and s < m: # ahtung!
                s += 1
            if nums[s] <= nums[m]:
                if nums[s] <= target < nums[m]:
                    e = m
                else:
                    s = m + 1
            else:
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    e = m
        return False
