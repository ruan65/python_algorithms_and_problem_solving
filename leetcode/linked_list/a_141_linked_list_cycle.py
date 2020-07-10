# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         try:
#             tortoise = head.next
#             hare = head.next.next
#             while tortoise is not hare:
#                 tortoise = tortoise.next
#                 hare = hare.next.next
#             return True
#         except:
#             return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
