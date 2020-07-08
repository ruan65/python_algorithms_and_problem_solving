class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_arr(node: TreeNode, dr) -> []:
    if not node:
        return [dr]
    return tree_to_arr(node.left, 'l') + [node.val] + tree_to_arr(node.right, 'r')


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        arr = tree_to_arr(root)
        print(arr)
        size = len(arr)
        if size == 1:
            return True
        if size % 2 == 0:
            return False
        mid = size // 2
        la, ra = arr[:mid], arr[mid + 1:]
        print(la)
        ra.reverse()
        print(ra)
        return la == ra


if __name__ == '__main__':
    # [1, 2,2, 3,4,4,3]
    # [1,2,2,2,null,2]
    t = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                 right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    # t = TreeNode(1, right=TreeNode(2, left=TreeNode(2)), left=TreeNode(2, right=TreeNode(2)))
    # t2 = TreeNode(1, left=TreeNode(2, right=TreeNode(3)))
    # print(f'left={t.left.val} right={t.right.val}')
    # swt = swap_tree(t)
    # print(f'left={t.left.val} right={t.right.val}')
    # t2sw = swap_tree(t2)
    # print(are_identical_trees(t, t2sw))

    print(Solution().isSymmetric(t))
