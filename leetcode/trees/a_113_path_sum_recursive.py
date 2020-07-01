class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(n: TreeNode) -> bool:
    return not n.left and not n.right


# def path_sum(node: TreeNode, k: int) -> [[int]]:
#     if not node:
#         return []
#     result = []
#     stack = [[node, []]]
#     while stack:
#         nd, path = stack.pop()
#         if is_leaf(nd) and sum(path) + nd.val == k:
#             path.append(nd.val)
#             result.append(path)
#         if nd.left:
#             cp = list.copy(path)
#             cp.append(nd.val)
#             stack.append([nd.left, cp])
#         if nd.right:
#             cp = list.copy(path)
#             cp.append(nd.val)
#             stack.append([nd.right, cp])
#     return result

def path_sum(node: TreeNode, k: int) -> [[int]]:
    if not node:
        return []
    result = []
    stack = [(node, node.val, [node.val])]
    while stack:
        nd, sm, path = stack.pop()
        if is_leaf(nd) and sm == k:
            result.append(path)
        if nd.left:
            stack.append((nd.left, sm + nd.left.val, path + [nd.left.val]))
        if nd.right:
            stack.append((nd.right, sm + nd.right.val, path + [nd.right.val]))
    return result


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        return path_sum(root, sum)


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, left=TreeNode(12), right=TreeNode(7)),
                  right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().pathSum(tr, 15))
