# def merge_pair(i1: [int], i2: [int]) -> [int]:
#     return [min(i1[0], i2[0]), max(i1[1], i2[1])]
#
#
# def is_overlap(i1: [int], i2: [int]) -> bool:
#     front = max(i1[0], i2[0])
#     back = min(i1[1], i2[1])
#     return back >= front
#
#
# def merge_all_intervals(data: [[int]]) -> [[int]]:
#     result = list()
#     if not data:
#         return result
#     if len(data) == 1:
#         return data
#     data.sort()
#
#     result.append(data[0])
#     for i in range(1, len(data)):
#         if is_overlap(result[-1], data[i]):
#             result[-1] = merge_pair(result[-1], data[i])
#         else:
#             result.append(data[i])
#     return result


# class Solution:
#     def merge(self, intervals: [[int]]) -> [[int]]:
#         return merge_all_intervals(intervals)

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            if n[0] <= res[-1][-1]:
                res[-1][-1] = max(n[1], res[-1][-1])
            else:
                res.append(n)
        return res


if __name__ == '__main__':
    ivals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    print(Solution().merge(ivals))
