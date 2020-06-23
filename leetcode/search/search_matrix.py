mtrx = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 31, 34, 50],
    [65, 72, 72, 75]
]

# mtrx = [
#     [1], [2]
# ]

sr = -1
er = -1


def find_row(mt, trg: int):
    global sr, er
    print(f'sr={sr} er={er}')
    if sr == er:
        return sr
    mr = (sr + er) // 2

    if trg <= mt[mr][-1]:
        er = mr
    else:
        sr = mr + 1
    return find_row(mt, trg)


def search_in_arr(row: [int], target) -> bool:
    return target in row


class Solution:

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False
        global sr, er
        sr = 0
        er = len(matrix) - 1
        found = find_row(matrix, target)
        print(f'found={found}')
        return search_in_arr(matrix[found], target)


if __name__ == '__main__':
    print(f'found: {Solution().searchMatrix(mtrx, 165)}')
