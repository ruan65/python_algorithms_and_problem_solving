class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    if node.left and node.right:
        return 1 + max(get_height(node.left), get_height(node.right))
    elif node.left:
        return 1 + get_height(node.left)
    elif node.right:
        return 1 + get_height(node.right)
    return 1


def tree_to_array(node: TreeNode) -> [int]:
    if not node:
        return [None]
    return tree_to_array(node.left) + [node.val] + tree_to_array(node.right)


if __name__ == '__main__':
    # tr = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4, right=TreeNode(5)))
    tr = TreeNode(1)

    print(get_height(tr))

    # print(tree_to_array(tr))
