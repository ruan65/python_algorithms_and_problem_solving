class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh, rh = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + min(lh, rh) if min(lh, rh) > 0 else 1 + max(lh, rh)


if __name__ == '__main__':
    # [1,2,2,3,3,null,null,4,4]
    # [-9,-3,2,null,4,4,0,-6,null,-5]
    # t1 = TreeNode(-9, left=TreeNode(-3, right=TreeNode(4, left=TreeNode(-6))),
    #               right=TreeNode(2, left=TreeNode(4, right=TreeNode(-5)), right=TreeNode(0)))
    t1 = TreeNode(1, left=TreeNode(2))
    # print(not TreeNode(1) or not TreeNode(1).left)
    print(Solution().minDepth(t1))
