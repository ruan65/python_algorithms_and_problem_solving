# Definition for a binary tree node.
from queue import SimpleQueue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    q = SimpleQueue()
    q.put(root)
    ans = 0
    while not q.empty():
        for _ in range(q.qsize()):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        ans += 1
    return ans
