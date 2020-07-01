# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        def make_bst(data: [int], left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            left_node = make_bst(data, left, mid - 1)
            right_node = make_bst(data, mid + 1, right)
            return TreeNode(data[mid], left_node, right_node)

        if not nums:
            return None
        return make_bst(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    # [0,-3,9,-10,null,5]
    nmbs = [-10, -3, 0, 5, 9]

    solution = Solution().sortedArrayToBST(nmbs)
    print(solution.left.val)
