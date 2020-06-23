from leetcode.linked_list.list_node import ListNode


def is_cycled(head: ListNode) -> bool:
    if head.next is None:
        return False
    track = []
    curr = head
    while curr.next is not None:
        if curr.next in track:
            return True
        track.append(curr.next)
        curr = curr.next
    return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        return is_cycled(head)
