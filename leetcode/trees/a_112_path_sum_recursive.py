# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'node[{self.val} l: {self.left is not None} r: {self.right is not None}]'


class Solution:
    def hasPathSum(self, node: TreeNode, k: int) -> bool:
        def has(nd: TreeNode, m: int) -> bool:
            if not nd:
                return False
            if not nd.left and not nd.right:
                return m == nd.val
            return has(nd.left, m - nd.val) or has(nd.right, m - nd.val)
        return has(node, k)


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, right=TreeNode(7)), right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().hasPathSum(tr, 16))
