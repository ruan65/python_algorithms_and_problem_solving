class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

# def height(root):
#     mx = 0
#
#     def dfs(nd, h):
#         nonlocal mx
#         if nd is None:
#             mx = max(mx, h - 1)
#             return
#         dfs(nd.left, h + 1)
#         dfs(nd.right, h + 1)
#
#     dfs(root, 0)
#     return mx

# def height(root):
#     if not root:
#         return -1
#     return 1 + max(height(root.left), height(root.right))


"""
BFS iterative
"""
# from collections import deque
#
#
# def height(root):
#     if not root:
#         return -1
#     h = -1
#     q = deque()
#     q.append(root)
#
#     while True:
#         size = len(q)
#         if size == 0:
#             return h
#         while size:
#             nd = q.popleft()
#             if nd.left:
#                 q.append(nd.left)
#             if nd.right:
#                 q.append(nd.right)
#             size -= 1
#         h += 1

"""
DFS iterative
"""


def height(root):
    if not root:
        return -1
    h = 0
    path, work = [], []  # treat like a stack
    work.append(root)

    while work:
        nd = work[-1]
        if path and path[-1] == nd:
            h = max(h, len(path))
            work.pop()
            path.pop()
        else:
            path.append(nd)
            if nd.right:
                work.append(nd.right)
            if nd.left:
                work.append(nd.left)
    return h - 1


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
