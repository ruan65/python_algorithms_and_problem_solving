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


#
# class Solution {
#         public TreeNode sortedListToBST(ListNode head) {
#         if (head == null) {
#             return null;
#         }
#         ListNode temp = head;
#         ListNode fast = head;
#         ListNode slow = new ListNode(-1);
#         slow.next = head;
#         ListNode dummy = slow;
#         int i = 0;
#         while (temp.next != null) {
#             temp = temp.next;
#             i++;
#             if (i == 2) {
#                 fast = fast.next;
#                 dummy = dummy.next;
#                 i = 0;
#             }
#         }
#
#         TreeNode bst = new TreeNode(fast.val);
#         dummy.next = null;
#         bst.left = sortedListToBST(slow.next);
#         bst.right = sortedListToBST(fast.next);
#         return bst;
#     }
# }
class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        tmp = head
        fast = head
        slow = ListNode(-1)
        slow.next = head
        dummy = slow
        i = 0
        while tmp.next:
            tmp = tmp.next
            i += 1
            if i == 2:
                fast = fast.next
                dummy = dummy.next
                i = 0
        bst = TreeNode(fast.val)
        dummy.next = None
        bst.left = self.sortedListToBST(slow.next)
        bst.right = self.sortedListToBST(fast.next)
        return bst


if __name__ == '__main__':
    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=0, next=n2)

    print(Solution().sortedListToBST(n1))
