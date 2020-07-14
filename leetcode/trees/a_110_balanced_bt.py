# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def is_balanced(nd: TreeNode) -> (bool, int):
#     if not nd:
#         return True, 0
#     bl, hl = is_balanced(nd.left)
#     br, hr = is_balanced(nd.right)
#     h = max(hl, hr) + 1
#     bal = bl and br and abs(hl - hr) < 2
#     return bal, h
#
#
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         return is_balanced(root)[0]

def get_h(nd: TreeNode) -> int:
    if not nd:
        return 0
    return 1 + max(get_h(nd.left), get_h(nd.right))


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(get_h(root.left) - get_h(root.right)) < 2 \
               and self.isBalanced(root.left) and self.isBalanced(
            root.right)


if __name__ == '__main__':
    # [1,2,2,3,3,null,null,4,4]
    t1 = TreeNode(1, left=TreeNode(2))

    print(Solution().isBalanced(t1))
