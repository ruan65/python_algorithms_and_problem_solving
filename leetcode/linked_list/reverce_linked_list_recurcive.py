from leetcode.linked_list.list_node import ListNode
from leetcode.linked_list.reverce_linked_list import linked_to_list


def reverse_linked_list(curr, prev=None) -> ListNode:
    if not curr:
        return prev

    tmp = curr.next
    curr.next = prev
    return reverse_linked_list(tmp, curr)


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        return reverse_linked_list(head)


if __name__ == '__main__':
    print('hello my')
    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    rev = Solution().reverseList(head=n1)
    print(linked_to_list(rev))
