class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


# recursive
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def ins(self, cur, val):
#         if not cur:
#             cur = Node(val)
#         elif val > cur.info:
#             cur.right = self.ins(cur.right, val)
#         else:
#             cur.left = self.ins(cur.left, val)
#         return cur
#
#     def insert(self, val):
#         self.root = self.ins(self.root, val)


# iterative
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        cur = self.root

        while True:
            if val > cur.info:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.insert(arr[i])

    preOrder(tree.root)
