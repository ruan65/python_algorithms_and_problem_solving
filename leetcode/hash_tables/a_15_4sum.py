class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in d:
                    d[sum2].append((i, j))
                else:
                    d[sum2] = [(i, j)]

        result = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i != k and i != l and j != k and j != l:
                            flist = [nums[i], nums[j], nums[k], nums[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)


if __name__ == '__main__':
    data = [-1, 0, 1, 2, -1, -4]
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
