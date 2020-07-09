from collections import deque


class Solution:
    def findOrder(self, num: int, nodes: [[int]]) -> [int]:
        ts = []
        graph = {n: set() for n in range(num)}
        in_degree = {n: 0 for n in range(num)}
        for ch, pr in nodes:
            in_degree[ch] += 1
            graph[pr].add(ch)
        starts = deque([n for n in in_degree if in_degree[n] == 0])
        while starts:
            nd = starts.popleft()
            ts.append(nd)
            for v in graph[nd]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    starts.append(v)
        return ts if len(ts) == num else []


if __name__ == '__main__':
    print(Solution().findOrder(2, [[1, 0]]))
    # print(build_adj_list(5, [[0, 1], [1, 2], [2, 3], [3, 4], [3, 1], [2, 4]]))
