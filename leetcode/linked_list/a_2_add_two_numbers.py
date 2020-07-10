class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rem_val(n: int) -> (int, int):
    return n // 10, n % 10


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = 0
#         res = n = ListNode(0)
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             carry, val = divmod(carry, 10)
#             n.next = n = ListNode(val)
#         return res.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next


if __name__ == '__main__':
    rs = Solution().addTwoNumbers(ListNode(2, next=ListNode(5, next=ListNode(8))),
                                  ListNode(7, next=ListNode(2)))
    while rs:
        print(rs.val, end='->')
        rs = rs.next
