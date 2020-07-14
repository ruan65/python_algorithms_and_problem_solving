from collections import deque


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = range(len(grid))
        columns = range(len(grid[0]))

        def bfs(rw, cl):
            q = deque()
            q.append((rw, cl))
            while q:
                rw, cl = q.popleft()
                for dr in directions:
                    row = rw + dr[0]
                    col = cl + dr[1]
                    if row in rows and col in columns and grid[row][col] == '1':
                        grid[row][col] = '0'
                        q.append((row, col))

        for r in rows:
            for c in columns:
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'
                    bfs(r, c)
        return count


if __name__ == '__main__':
    gr = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0"],
    ]
    print(Solution().numIslands(gr))
