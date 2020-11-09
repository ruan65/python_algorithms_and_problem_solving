# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def get_sum(nd: TreeNode) -> int:
#     if not nd:
#         return 0
#     if nd.left is nd.right:
#         return nd.val
#     if not nd.left and nd.right:
#         return nd.val + get_sum(nd.right)
#     if not nd.right and nd.left:
#         return nd.val + get_sum(nd.left)
#     return nd.val + get_sum(nd.left) + get_sum(nd.right)
#
#
# def get_tilt(nd: TreeNode) -> int:
#     if nd.left is nd.right:
#         return 0
#     return abs(get_sum(nd.left) - get_sum(nd.right))
#
#
# class Solution:
#     tilt = 0
#
#     def findTilt(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         self.tilt += get_tilt(root)
#         if root.left:
#             self.findTilt(root.left)
#         if root.right:
#             self.findTilt(root.right)
#         return self.tilt

class Solution:
    sum = 0

    def findTilt(self, root: TreeNode) -> int:
        def get_sum(nd):
            if not nd:
                return 0
            sleft, sright = get_sum(nd.left), get_sum(nd.right)
            self.sum += abs(sleft - sright)
            return nd.val + sleft + sright

        get_sum(root)
        return self.sum
