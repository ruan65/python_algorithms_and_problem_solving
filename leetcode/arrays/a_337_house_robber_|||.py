# Definition for a binary tree node.
from trees.save_tree_to_array import restore_tree_from_arr


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


count = 0


def rb(rt: TreeNode) -> [[int]]:
    global count
    count += 1
    if not rt:
        return 0, 0
    left: [[int]] = rb(rt.left)
    right: [[int]] = rb(rt.right)
    result = [0, 0]
    result[0] = max(left[0], left[1]) + max(right[0], right[1])
    result[1] = rt.val + left[0] + right[0]
    return result


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(rb(root))


if __name__ == '__main__':
    inp = [1, 2, 10, 0, 7, 0, 1, 4, 5, 0, 1, 1, 2, 3, 4, 5, 0, 0, 0, 0, 3]
    tr = restore_tree_from_arr(inp, None, 0, len(inp))
    print(Solution().rob(tr))
    print(count)
