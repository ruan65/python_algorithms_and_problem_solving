class Solution:
    def combine(self, number: int, k: int) -> [[int]]:

        def dfs(index: int,  w: int, chosen: [int]):
            if w == 0:
                res.append(chosen[:])
                return

            for i in range(index, number + 1):
                # choose
                chosen.append(i)
                # explore
                dfs(i + 1, w - 1, chosen)
                # unchoose
                chosen.pop()

        res = []
        dfs(1, k, [])
        return res


if __name__ == '__main__':
    print(Solution().combine(4, 2))
