from leetcode.linked_list.list_node import ListNode


def is_cycled(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    p1 = head
    p2 = head.next

    while p1 != p2:
        if not p2 or not p2.next:
            return False
        p1 = p1.next
        p2 = p2.next.next
    return True

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        return is_cycled(head)
