class Solution:
    def solve(self, board: [[str]]) -> None:
        if not board:
            return
        rows = range(len(board))
        columns = range(len(board[0]))

        def dfs(rw, cl):
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if rw in rows and cl in columns and board[rw][cl] == "O":
                board[rw][cl] = "R"
                for d in dirs:
                    dfs(rw + d[0], cl + d[1])

        for r in rows:
            dfs(r, 0)
            dfs(r, columns[-1])
        for c in columns:
            dfs(0, c)
            dfs(rows[-1], c)

        for r in rows:
            for c in columns:
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "R":
                    board[r][c] = "O"


if __name__ == '__main__':
    brd = [
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "O", "X"]
    ]

    print(brd)

    Solution().solve(brd)

    print(brd)
