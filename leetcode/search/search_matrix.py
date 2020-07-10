class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        s, e = 0, m * n

        while s < e:
            mid = (s + e) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                s = mid + 1
            else:
                e = mid
        return False
