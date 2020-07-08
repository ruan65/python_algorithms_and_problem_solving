class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        answer = []

        def dfs_fill(nd: TreeNode, pth: [], k: int):
            if not nd:
                return
            if not nd.left and not nd.right:
                if nd.val == k:
                    rs = pth[:]
                    rs.append(nd.val)
                    answer.append(rs)
                return
            dfs_fill(nd.left, pth + [nd.val], k - nd.val)
            dfs_fill(nd.right, pth + [nd.val], k - nd.val)

        dfs_fill(root, [], sum)
        return answer


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, left=TreeNode(12), right=TreeNode(7)),
                  right=TreeNode(10, left=TreeNode(4), right=TreeNode(1)))
    print(Solution().pathSum(tr, 15))
