from leetcode.linked_list.list_node import ListNode


def linked_to_list(linked: ListNode) -> [int]:
    if not linked:
        return []
    result = [linked.val]
    current = linked
    while current.next is not None:
        result.append(current.next.val)
        current = current.next
    return result


def flatten_linked_lists_array(lists: [ListNode]) -> [int]:
    result: [int] = []
    for node in lists:
        result += linked_to_list(node)
    return result


def list_to_linked(lst: []) -> ListNode:
    if len(lst) == 0:
        return None

    result = ListNode(val=lst[0])

    for i in range(1, len(lst)):
        result = ListNode(lst[i], result)

    return result


def merge_and_sort(lists: [ListNode]):
    arr: [int] = flatten_linked_lists_array(lists)
    arr.sort()
    arr.reverse()
    return list_to_linked(arr)


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists or len(lists) == 0 or (len(lists) == 1 and not lists[0]):
            return None
        return merge_and_sort(lists)
