# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'node[{self.val} l: {self.left is not None} r: {self.right is not None}]'


def has_path_sum_rec(node: TreeNode, k: int) -> bool:
    if not node:
        return False
    if not node.left and not node.right:
        return node.val == k
    return has_path_sum_rec(node.right, k - node.val) or has_path_sum_rec(node.left, k - node.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return has_path_sum_rec(root, sum)


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, right=TreeNode(7)), right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().hasPathSum(tr, 16))
