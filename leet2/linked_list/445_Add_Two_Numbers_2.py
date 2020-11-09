class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_int(nd: ListNode) -> int:
    n = 0
    while nd:
        n = n * 10 + nd.val
        nd = nd.next
    return n


def to_list(n: int) -> ListNode:
    head = ListNode(n % 10)
    n //= 10
    while n:
        tmp = head
        head = ListNode(n % 10, tmp)
        n //= 10
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return to_list(to_int(l1) + to_int(l2))
