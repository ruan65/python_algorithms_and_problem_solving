# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def linked_to_arr(self, h: ListNode, ds: [int]) -> [int]:
        if not h:
            return ds
        ds.append(h.val)
        if h.next:
            return self.linked_to_arr(h.next, ds)
        return ds

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        sorted_data = self.linked_to_arr(head, [])

        def make_bst(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = start + (end - start) // 2
            return TreeNode(sorted_data[mid], left=make_bst(start, mid - 1), right=make_bst(mid + 1, end))

        return make_bst(0, len(sorted_data) - 1)


if __name__ == '__main__':
    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=0, next=n2)

    print(Solution().linked_to_arr(n1, []))

    print(Solution().sortedListToBST(n1))
