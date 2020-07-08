from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        fmap = defaultdict(int)
        for n in nums:
            fmap[n] += 1
        mf = max(fmap.values())
        lns = {k: [] for k, v in fmap.items() if v == mf}
        for i in range(len(nums)):
            if nums[i] in lns:
                lns[nums[i]].append(i)
        return min([h[-1] - h[0] + 1 for h in lns.values()])


if __name__ == '__main__':
    ar = [1, 2, 2, 7, 3, 7, 1, 7, 1]
    print(Solution().findShortestSubArray(ar))
