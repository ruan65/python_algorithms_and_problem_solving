from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def maxLevelSum(self, root: TreeNode) -> int:
#         levels: [int] = []
#         q = deque()
#         q.append(root)
#         while q:
#             lvl = []
#             while q:
#                 lvl.append(q.popleft())
#             levels.append(sum([n.val if n else 0 for n in lvl]))
#             for lv in lvl:
#                 if lv:
#                     q.append(lv.left)
#                     q.append(lv.right)
#         max_val = max(levels)
#         print(levels)
#         return levels.index(max_val) + 1

# bfs iter
# class Solution:
#     def maxLevelSum(self, root: TreeNode) -> int:
#         mx, lvl, mx_lvl = -2**31, 0, 0
#         q = deque()
#         q.append(root)
#         while q:
#             lvl += 1
#             curr = 0
#             for _ in range(len(q)):
#                 nd = q.popleft()
#                 curr += nd.val
#                 if nd.left:
#                     q.append(nd.left)
#                 if nd.right:
#                     q.append(nd.right)
#             if mx < curr:
#                 mx, mx_lvl = curr, lvl
#         return mx_lvl

# dfs recursive
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, lvl: int):
            if not node:
                return
            if len(lvls) == lvl:
                lvls.append(node.val)
            else:
                lvls[lvl] += node.val
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        lvls = [root.val]
        dfs(root, 0)
        return lvls.index(max(lvls)) + 1



def restore_tree_from_arr(lst: [int], root: TreeNode, i: int, n: int) -> TreeNode:
    if i < n:
        root = TreeNode(lst[i])
        root.left = restore_tree_from_arr(lst, root.left, 2 * i + 1, n)
        root.right = restore_tree_from_arr(lst, root.right, 2 * i + 2, n)
    return root


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, right=TreeNode(7)),
                  right=TreeNode(10, right=TreeNode(1)))
    # arr = [1, 7, 0, 7, -8, None, None]
    # tree = restore_tree_from_arr(arr, None, 0, len(arr))
    print(Solution().maxLevelSum(tr))
