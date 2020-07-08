# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_depth(node: TreeNode) -> int:
    if not node:
        return 0
    lt = 1 + get_depth(node.left)
    rt = 1 + get_depth(node.right)
    return max(lt, rt)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return get_depth(root)