from trees.get_level_of_el_of_the_tree import TreeNode


#
#
# def are_nodes_symmetric(lt: TreeNode, rt: TreeNode) -> bool:
#     if not lt or not rt:
#         return lt == rt
#     if lt.val != rt.val:
#         return False
#
#     return are_nodes_symmetric(lt.left, rt.right) and are_nodes_symmetric(lt.right, rt.left)
#
#
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#
#         return are_nodes_symmetric(root.left, root.right)

def sym(p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and sym(p.left, q.right) and sym(p.right, q.left)
    return p is q


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return sym(root.left, root.right)

# works fine
