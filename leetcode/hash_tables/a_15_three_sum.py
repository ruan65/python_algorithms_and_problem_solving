# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# def arr_to_dict(arr):
#     res = defaultdict(int)
#     for e in arr:
#         res[e] += 1
#     return res
#
# def find_pair()
from leetcode.hash_tables.big_data import big_list


def find_target_sum_indexes(arr: [int], target: int) -> [[int]]:
    ht = {}
    result = []
    for i in range(len(arr)):
        if target - arr[i] in ht:
            result.append([i, ht[target - arr[i]]])
        ht[arr[i]] = i
    return result


def find_triplets(arr: [int]) -> [[int]]:
    if len(arr) > 2 and set(arr) == {0}:
        return [[0, 0, 0]]
    tracker: [{int}] = []
    for i in range(len(arr)):
        d = 0 - arr[i]
        ind: [[int]] = find_target_sum_indexes(arr, d)
        for el in ind:
            if len(el) == 2 and i not in el:
                trp = {arr[i], arr[el[0]], arr[el[1]]}
                if trp not in tracker:
                    tracker.append(trp)
    answer = []
    for s in tracker:
        if len(s) == 3:
            answer.append(list(s))
        if len(s) == 1 and sum(s) == 0:
            answer.append([0, 0, 0])
        if len(s) == 2:
            sl = list(s)
            if sl[0] * 2 + sl[1] == 0:
                sl.append(sl[0])
            elif sl[1] * 2 + sl[0] == 0:
                sl.append(sl[1])
            if sum(sl) == 0:
                answer.append(sl)

    return answer


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        return find_triplets(nums)


if __name__ == '__main__':
    # data = [-1, 0, 1, 2, -1, -4]
    # data = [0, 0, 0, 0]
    # data = [0, 0, 0, 0]
    # data = [-1, 0, 1]
    # data = [1, 2, -2, -1]
    # data = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    data = [0, 4, 0, -2, 3, 1, -5, 0]
    # data = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    print(find_triplets(big_list))
