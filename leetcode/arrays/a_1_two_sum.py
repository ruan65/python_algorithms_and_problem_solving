arr = [2, 5, 5, 11]

trg = 10


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hm: {int: int} = {}
        for i,n in enumerate(nums):
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
        return [-1, -1]

