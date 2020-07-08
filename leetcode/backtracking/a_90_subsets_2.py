class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        res = [[]]
        for n in nums:
            for sbs in [subset + [n] for subset in res]:
                sbs.sort()
                if sbs not in res:
                    res.append(sbs)
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
