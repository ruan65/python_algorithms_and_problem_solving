class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(node: TreeNode) -> [int]:
    if not node:
        return []
    elif not node.left and not node.right:
        return [node.val]
    elif not node.left:
        return [None, node.val] + tree_to_list(node.right)
    elif not node.right:
        return tree_to_list(node.left) + [node.val, None]
    else:
        return tree_to_list(node.left) + [node.val] + tree_to_list(node.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p and not q:
    #         return True
    #     if (p and not q) or (not p and q):
    #         return False
    #     return tree_to_list(p) == tree_to_list(q)


# [1, 1]
# [1, null, 1]

if __name__ == '__main__':
    # t1 = TreeNode(1, right=TreeNode(2, left=TreeNode(2, right=TreeNode(3))))
    # t2 = TreeNode(1, right=TreeNode(4, left=TreeNode(4, right=TreeNode(3))))

    t1 = TreeNode(1, left=TreeNode(1))
    t2 = TreeNode(1, right=TreeNode(1))
    print(Solution().isSameTree(t1, t2))

    print(tree_to_list(t1))
    print(tree_to_list(t2))
