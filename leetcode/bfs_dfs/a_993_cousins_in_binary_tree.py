class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(rt: TreeNode, v: int, k: int, pr: TreeNode) -> (bool, int, TreeNode):
    if rt.val == v:
        return True, k, pr
    if rt.left:
        ls = search(rt.left, v, k + 1, rt)
        if ls:
            return ls
    if rt.right:
        rs = search(rt.right, v, k + 1, rt)
        if rs:
            return rs


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        x_res = search(root, x, 0, None)
        y_res = search(root, y, 0, None)
        if not (x_res[0] and y_res[0]):
            return False
        if x_res[1] == y_res[1] and x_res[2] != y_res[2]:
            return True
        return False


if __name__ == '__main__':
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2, right=n4)
    n3 = TreeNode(3, right=n5)
    n1 = TreeNode(1, left=n2, right=n3)
    root = n1

    fnd = search(root, 4, 0, None)

    print(fnd)
    print(fnd[2].val)

    print(f'is cousins: {Solution().isCousins(root, 2, 3)}')
