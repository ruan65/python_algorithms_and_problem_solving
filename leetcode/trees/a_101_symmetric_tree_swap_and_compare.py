import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def are_identical_trees(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False

    return are_identical_trees(p.left, q.left) and are_identical_trees(p.right, q.right)


def swap_tree(tr: TreeNode) -> TreeNode:
    if not tr or (not tr.left and not tr.right):
        return tr
    sw_left = swap_tree(tr.left)
    sw_right = swap_tree(tr.right)
    tr.right = sw_left
    tr.left = sw_right
    return tr


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        cp = copy.deepcopy(root)
        return are_identical_trees(root, swap_tree(cp))


if __name__ == '__main__':
    t = TreeNode(1, right=TreeNode(2, left=TreeNode(3)), left=TreeNode(2, left=TreeNode(3)))
    # t2 = TreeNode(1, left=TreeNode(2, right=TreeNode(3)))
    # print(f'left={t.left.val} right={t.right.val}')
    # swt = swap_tree(t)
    # print(f'left={t.left.val} right={t.right.val}')
    # t2sw = swap_tree(t2)
    # print(are_identical_trees(t, t2sw))

    print(Solution().isSymmetric(t))
