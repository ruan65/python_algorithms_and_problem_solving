from leetcode.linked_list.list_node import ListNode


def linked_to_list(linked: ListNode) -> []:
    result = [linked.val]
    current = linked
    while current.next is not None:
        result.append(current.next.val)
        current = current.next
    return result


def list_to_linked(lst: []) -> ListNode:
    if len(lst) == 0:
        return ListNode()

    result = ListNode(val=lst[0])

    for i in range(1, len(lst)):
        result = ListNode(lst[i], result)

    return result


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        ints = linked_to_list(head)

        return list_to_linked(ints)

