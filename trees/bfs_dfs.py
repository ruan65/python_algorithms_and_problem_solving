class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(node: TreeNode) -> [int]:
    values = []
    if not node:
        return values
    queue = [node]
    while queue:
        nd = queue.pop(0)
        values.append(nd.val)
        if nd.left:
            queue.append(nd.left)
        if nd.right:
            queue.append(nd.right)
    return values


def bfs_sum(node: TreeNode) -> int:
    if not node:
        return 0
    queue = [node]
    sm = 0
    while queue:
        nd = queue.pop(0)
        print(nd.val, end='->')
        sm += nd.val
        if nd.left:
            queue.append(nd.left)
        if nd.right:
            queue.append(nd.right)
    return sm


def dfs_sum_recursive(node: TreeNode) -> int:
    if not node:
        return 0
    print(node.val, end='*>')
    return node.val + dfs_sum_recursive(node.left) + dfs_sum_recursive(node.right)


def bfs_sum_recursive(node: TreeNode) -> int:
    if not node:
        return 0
    print(node.val, end='*>')
    return bfs_sum_recursive(node.right) + node.val + bfs_sum_recursive(node.left)


def dfs_sum(node: TreeNode) -> int:
    if not node:
        return 0
    stack = [node]
    sm = 0
    while stack:
        nd = stack.pop()
        print(nd.val, end='=>')
        sm += nd.val
        if nd.right:
            stack.append(nd.right)
        if nd.left:
            stack.append(nd.left)

    return sm


def dfs_sum_right_to_left(node: TreeNode) -> int:
    if not node:
        return 0
    stack = [node]
    sm = 0
    while stack:
        nd = stack.pop()
        print(nd.val, end='=>')
        sm += nd.val
        if nd.left:
            stack.append(nd.left)
        if nd.right:
            stack.append(nd.right)
    return sm


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(6)),
                  right=TreeNode(4, left=TreeNode(7), right=TreeNode(5)))

    print(bfs(tr))
    print(bfs_sum(tr))
    print('\n')
    print(dfs_sum(tr))
    print('\n')
    print(dfs_sum_right_to_left(tr))
    print('***************** recursive')
    print('dfs')
    print(dfs_sum_recursive(tr))
    print('bfs')
    print(bfs_sum_recursive(tr))
