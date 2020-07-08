# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

from collections import defaultdict


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        dd = defaultdict(int)

        for e in nums:
            dd[e] += 1

        for k, v in dd.items():
            if v == 1:
                return k
