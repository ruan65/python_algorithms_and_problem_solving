import collections


class Solution:

    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        num_columns = range(len(grid))
        num_rows = range(len(grid[0]))

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if r in num_columns and c in num_rows and grid[r][c] == '1':
                        queue.append((r, c))
                        grid[r][c] = '0'

        for i in num_columns:
            for j in num_rows:
                if grid[i][j] == '1':
                    grid[i][j] = '0'  # make it as visited
                    bfs(i, j)
                    count += 1
        return count
        # rows, cols = len(grid), len(grid[0])
        # count = 0
        #
        # def bfs(rw, cl):
        #     q = collections.deque()
        #
        #     q.append((rw, cl))
        #     while q:
        #         rw, cl = q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #         for dr, dc in directions:
        #             r, c = (rw + dr, cl + dc)
        #             if r in range(rows) and c in range(cols) and grid[r][c] == '1':
        #                 grid[rw][cl] = '*'
        #                 q.append((r, c))
        #
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1':
        #             grid[row][col] = '*'
        #             bfs(row, col)
        #             count += 1
        # return count


if __name__ == '__main__':
    # gr = [
    #     ['1', '1', '0', '1'],
    #     ['1', '0', '0', '1'],
    #     ['1', '0', '1', '1'],
    #     ['0', '0', '1', '1'],
    #     ['1', '0', '1', '1'],
    # ]

    # gr = [
    #     ['1', '1', '0', '1'],
    #     ['1', '1', '0', '1'],
    # ]

    gr = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    solution = Solution()
    res = solution.numIslands(gr)
    print(res)
