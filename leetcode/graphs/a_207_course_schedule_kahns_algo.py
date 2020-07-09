from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        in_degree = defaultdict(set)
        out_degree = defaultdict(set)
        conn_rem = 0
        zero_ind = deque()
        for x, y in prerequisites:
            out_degree[y].add(x)
            in_degree[x].add(y)
        for cr in range(numCourses):
            if not in_degree[cr]:
                zero_ind.append(cr)
                conn_rem += 1
        while zero_ind:
            nd = zero_ind.popleft()
            for n in out_degree[nd]:
                in_degree[n].remove(nd)
                if not in_degree[n]:
                    zero_ind.append(n)
                    conn_rem += 1

        return conn_rem == numCourses


if __name__ == '__main__':
    print(Solution().canFinish(5, [[0, 1], [1, 2], [2, 3], [3, 4], [3, 1], [2, 4]]))
