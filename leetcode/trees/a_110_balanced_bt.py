# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(nd: TreeNode) -> (bool, int):
    if not nd:
        return True, 0
    bl, hl = is_balanced(nd.left)
    br, hr = is_balanced(nd.right)
    h = max(hl, hr) + 1
    bal = bl and br and abs(hl - hr) < 2
    return bal, h


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return is_balanced(root)[0]


if __name__ == '__main__':
    # [1,2,2,3,3,null,null,4,4]
    t1 = TreeNode(1, left=TreeNode(2))

    print(is_balanced(t1))
