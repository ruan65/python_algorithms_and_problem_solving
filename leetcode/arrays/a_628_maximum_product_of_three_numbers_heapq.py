import heapq


class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        hmn = heapq.nsmallest(2, nums)
        hmx = heapq.nlargest(3, nums)
        return max(hmx[0] * hmx[1] * hmx[2], hmn[0] * hmn[1] * hmx[0])
