from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(node: TreeNode) -> int:
    """single node height is 1"""
    if not node:
        return 0
    if node.left and node.right:
        return 1 + max(get_height(node.left), get_height(node.right))
    elif node.left:
        return 1 + get_height(node.left)
    elif node.right:
        return 1 + get_height(node.right)
    return 1


def tree_size(node: TreeNode) -> int:
    return pow(2, get_height(node)) - 1


def save_tree_to_arr(node: TreeNode) -> []:
    if not node:
        return []
    result = [node.val]
    queue = deque()
    queue.append(node)
    while queue:
        nd = queue.popleft()
        if nd.left:
            queue.append(nd.left)
            result.append(nd.left.val)
        else:
            result.append(None)
        if nd.right:
            queue.append(nd.right)
            result.append(nd.right.val)
        else:
            result.append(None)

    while result[-1] is None:
        result.pop()
    return result


def restore_tree_from_arr(lst: [int], root: TreeNode, i: int, n: int) -> TreeNode:
    if i < n:
        root = TreeNode(lst[i])
        root.left = restore_tree_from_arr(lst, root.left, 2 * i + 1, n)
        root.right = restore_tree_from_arr(lst, root.right, 2 * i + 2, n)
    return root


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, right=TreeNode(7)),
                  right=TreeNode(10, right=TreeNode(1)))
    # print(tree_size(tr))
    arr = save_tree_to_arr(tr)
    print(arr)
    restored_tree = restore_tree_from_arr(arr, None, 0, len(arr))
    print(save_tree_to_arr(restored_tree))
