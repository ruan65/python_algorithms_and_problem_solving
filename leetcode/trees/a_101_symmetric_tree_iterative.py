from trees.get_level_of_el_of_the_tree import TreeNode


# ITERATIVE
def is_symmetric_iterative(self, root: TreeNode) -> bool:
    if not root:
        return True
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()
        if not left and not right:
            continue
        elif not left or not right or left.val != right.val:
            return False
        stack.append([left.left, right.right])
        stack.append([left.right, right.left])
    return True

# works fine
