from trees.get_level_of_el_of_the_tree import TreeNode


# ITERATIVE
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        stack.append((root.left, root.right))

        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

        return True

# works fine
