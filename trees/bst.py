class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Node = left
        self.right: Node = right

    def insert(self, data) -> bool:
        if self.val == data:
            return False
        elif self.val > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.val))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.val))
            if self.right:
                self.right.inorder()

    def get_height(self) -> int:
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.right:
            return 1 + self.right.get_height()
        elif self.left:
            return 1 + self.left.get_height()
        return 1


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data) -> bool:
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def get_height(self) -> int:
        if self.root:
            return self.root.get_height()
        else:
            return 0

    def preorder(self):
        print('preorder')
        self.root.pr_eorder()

    def postorder(self):
        print('postorder')
        self.root.postorder()

    def inorder(self):
        print('inorder')
        self.root.inorder()


if __name__ == '__main__':
    bst = Tree()
    print(f'bst height={bst.get_height()}')
    bst.insert(10)
    print(f'bst height={bst.get_height()}')
    print(bst.insert(2))
    print(f'bst height={bst.get_height()}')
    bst.insert(13)
    print(f'bst height={bst.get_height()}')
    bst.insert(4)
    print(f'bst height={bst.get_height()}')
    bst.insert(15)
    bst.insert(25)
    bst.insert(26)
    bst.insert(3)


    print(bst.preorder())
    print(bst.postorder())
    print(bst.inorder())
    print(f'bst height={bst.get_height()}')
