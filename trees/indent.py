from trees.bfs_dfs import TreeNode


def is_leaf(nd: TreeNode) -> bool:
    return not nd.left and not nd.right


def has_path_sum(node: TreeNode, k: int) -> bool:
    if not node:
        return False

    stack = []
    stack.append((node, False, False))
    sm = node.val
    while stack:
        nd, lv, rv = stack[-1]
        if not is_leaf and lv and rv:
            stack.pop()
            continue
        if is_leaf(nd):
            stack.pop()
            return nd.val == k
        if nd.left and not lv:
            stack[-1][1] = True
            stack.append(nd.left)
        if nd.right and not rv:
            stack[-1][2] = True
            stack.append(nd.right)
    return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return has_path_sum(root, sum)
