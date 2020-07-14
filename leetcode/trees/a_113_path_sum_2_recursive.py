class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        res = []
        if not root:
            return res

        def fill(nd: TreeNode, path: list, rem: int):
            if not nd.left and not nd.right and rem == nd.val:
                path.append(nd.val)
                res.append(path)
            if nd.left:
                fill(nd.left, path + [nd.val], rem - nd.val)
            if nd.right:
                fill(nd.right, path + [nd.val], rem - nd.val)

        fill(root, [], sum)
        return res


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, left=TreeNode(12), right=TreeNode(7)),
                  right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().pathSum(tr, 15))
