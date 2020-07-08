class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return

        def dfs(nd):
            for nb in nd.neighbors:
                if nb not in hm:
                    cp = Node(nb.val)
                    hm[nb] = cp
                    hm[nd].neighbors.append(cp)
                    dfs(nb)
                else:
                    hm[nd].neighbors.append(hm[nb])

        copy = Node(val=node.val)
        hm = {node: copy}
        dfs(node)
        return copy


if __name__ == '__main__':
    n1 = Node(val=1, neighbors=[Node(val=2), Node(val=3)])
    print(Solution().cloneGraph(n1))
