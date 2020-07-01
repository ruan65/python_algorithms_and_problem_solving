class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pr_eorder(nd: TreeNode):
    if not nd:
        return
    print(nd.val, end='->')
    pr_eorder(nd.left)
    pr_eorder(nd.right)


def in_order(nd: TreeNode):
    if not nd:
        return
    in_order(nd.left)
    print(nd.val, end='->')
    in_order(nd.right)


def post_order(nd: TreeNode):
    if not nd:
        return
    post_order(nd.left)
    post_order(nd.right)
    print(nd.val, end='->')


if __name__ == '__main__':
    tr = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4, right=TreeNode(5)))
    print('pre order')
    pr_eorder(tr)
    print('\nin order')
    in_order(tr)
    print('\npost order')
    post_order(tr)
