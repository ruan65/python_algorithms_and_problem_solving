class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: TreeNode) -> int:
    if not node:
        return 0
    max_d = 0
    stack = [(node, 1)]
    while stack:
        nd, d = stack.pop()
        if d > max_d:
            max_d = d
        if nd.left:
            stack.append((nd.left, d + 1))
        if nd.right:
            stack.append((nd.right, d + 1))
    return max_d


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return dfs(root)
