class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()

        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i - 1]:
                continue
            st = set()
            for v2 in nums[i + 1:]:
                if v2 not in st:
                    st.add(-v - v2)
                else:
                    res.add((v, v2, -v - v2))

        return list(map(list, res))


if __name__ == '__main__':
    data = [-1,0,1,2,-1,-4]
    # data = [1, 1, -2]
    # data = [0, 0, 0]
    # data = [0, 0, 0, 0]
    # data = [-1, 0, 1]
    # data = [1, 2, -2, -1]
    # data = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # data = [0, 4, 0, -2, 3, 1, -5, 0]
    # data = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    # data = [1, -1, -1, 0]
    # data = [2, 0, -2, -5, -5, -3, 2, -4]
    print(Solution().threeSum(data))
    # print(find_3sum(big_list))
