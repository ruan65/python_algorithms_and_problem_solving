class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#
#         if not p and not q:
#             return True
#
#         if (p and not q) or (not p and q):
#             return False
#
#         if (not p.left and not p.right) and (not q.left and not q.right):
#             return p.val == q.val
#
#         if ((p.left and not q.left) or (not p.left and q.left)) or (
#                 (p.right and not q.right) or (not p.right and q.right)):
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


# [1, null, 2, 4, null, null, 3]
# [1, null, 4, 2, null, null, 3]

if __name__ == '__main__':
    t1 = TreeNode(1, right=TreeNode(2, left=TreeNode(2, right=TreeNode(3))))
    t2 = TreeNode(1, right=TreeNode(4, left=TreeNode(4, right=TreeNode(3))))

    print(Solution().isSameTree(t1, t2))
