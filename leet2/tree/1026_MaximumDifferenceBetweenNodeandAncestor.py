# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     res = 0
#
#     def maxAncestorDiff(self, root: TreeNode) -> int:
#         def diff(nd, mx, mn):
#             if not nd:
#                 return
#             self.res = max(self.res, abs(mx - nd.val), abs(mn - nd.val))
#             mx, mn = max(mx, nd.val), min(mn, nd.val)
#             diff(nd.left, mx, mn)
#             diff(nd.right, mx, mn)
#
#         diff(root, root.val, root.val)
#         return self.res

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def diff(nd, mx, mn):
            if not nd:
                return mx - mn
            mx, mn = max(mx, nd.val), min(mn, nd.val)
            return max(diff(nd.left, mx, mn), diff(nd.right, mx, mn))

        return diff(root, root.val, root.val)
