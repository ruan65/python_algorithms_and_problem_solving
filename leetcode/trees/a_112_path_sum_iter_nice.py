# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'node[{self.val} l: {self.left is not None} r: {self.right is not None}]'


def is_leaf(nd: TreeNode) -> bool:
    return not nd.left and not nd.right


def has_path_sum(node: TreeNode, k: int) -> bool:
    if not node:
        return False

    stack = list()
    stack.append([node, node.left is None, node.right is None])
    sm = node.val
    while stack:
        tpl = stack[-1]
        nd, lv, rv = tpl[0], tpl[1], tpl[2]
        if not is_leaf(nd) and lv and rv:
            lf, _, __ = stack.pop()
            sm -= lf.val
            continue
        if is_leaf(nd):
            lf, _, __ = stack.pop()
            if sm == k:
                return True
            else:
                sm -= lf.val
                continue
        if nd.left and not lv:
            stack[-1][1] = True
            stack.append([nd.left, nd.left.left is None, nd.left.right is None])
            sm += nd.left.val
            continue
        if nd.right and not rv:
            stack[-1][2] = True
            stack.append([nd.right, nd.right.left is None, nd.right.right is None])
            sm += nd.right.val
            continue
    return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return has_path_sum(root, sum)


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, right=TreeNode(7)), right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().hasPathSum(tr, 16))
