def build_adj_list(n: int, edges: [[int]]) -> [[int]]:
    adj_list = [[] for _ in range(n)]
    for n1, n2 in edges:
        adj_list[n2].append(n1)
    return adj_list


class Solution:
    def canFinish(self, num: int, edges: [[int]]) -> bool:
        adj = build_adj_list(num, edges)
        state = [0 for _ in range(num)]  # 0 - unvisited, 1 - being process, -1 - visited

        def has_cycle(v) -> bool:
            if state[v] == 1:
                return False
            if state[v] == -1:
                return True
            state[v] = -1
            for nd in adj[v]:
                if has_cycle(nd):
                    return True

            state[v] = 1
            return False

        for node in range(num):
            if has_cycle(node):
                return False
        return True


if __name__ == '__main__':
    print(Solution().canFinish(5, [[1], [2], [3, 4], [4, 1], []]))
