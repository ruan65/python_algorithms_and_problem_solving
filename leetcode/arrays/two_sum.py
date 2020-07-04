arr = [2, 5, 5, 11]

trg = 10


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

def two_sum(nums, target):
    for i in range(len(nums)):
        for e in range(i + 1, len(nums)):
            if nums[i] + nums[e] == target:
                return [i, e]


print(two_sum(arr, trg))
