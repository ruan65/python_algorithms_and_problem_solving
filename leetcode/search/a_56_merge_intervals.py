def merge_pair(i1: [int], i2: [int]) -> [int]:
    return [min(i1[0], i2[0]), max(i1[1], i2[1])]


def is_overlap(i1: [int], i2: [int]) -> bool:
    front = max(i1[0], i2[0])
    back = min(i1[1], i2[1])
    return back >= front


def merge_all_intervals(data: [[int]]) -> [[int]]:
    stack = list()
    if not data:
        return stack
    if len(data) == 1:
        return data
    data.sort()

    stack.append(data[0])
    for i in range(1, len(data)):
        if is_overlap(stack[-1], data[i]):
            stack[-1] = merge_pair(stack[-1], data[i])
        else:
            stack.append(data[i])
    return stack


class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        return merge_all_intervals(intervals)


if __name__ == '__main__':
    ivals = [[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]

    print(merge_all_intervals(ivals))
