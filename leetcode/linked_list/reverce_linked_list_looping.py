from leetcode.linked_list.list_node import ListNode
from leetcode.linked_list.reverce_linked_list import linked_to_list


# [1 -> 2 -> 3]


def reverse_linked_list(lst: ListNode) -> ListNode:
    if lst is None or lst.next is None:
        return lst

    prev = None
    curr = lst

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_linked_list(head)


if __name__ == '__main__':
    print('hello my')
    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    rev = Solution().reverseList(head=n1)
    print(linked_to_list(rev))
