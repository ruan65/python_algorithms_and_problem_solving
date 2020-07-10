class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         n1 = n2 = ''
#         while l1:
#             n1 += str(l1.val)
#             l1 = l1.next
#         while l2:
#             n2 += str(l2.val)
#             l2 = l2.next
#         s = str(int(n1) + int(n2))
#         answ = nxt = ListNode()
#         for d in s:
#             nxt.next = ListNode(int(d))
#             nxt = nxt.next
#         return answ.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = ''
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        nmb = int(n1) + int(n2)
        answ = ListNode(nmb % 10)
        nmb //= 10
        while nmb:
            answ = ListNode(nmb % 10, answ)
            nmb //= 10
        return answ
