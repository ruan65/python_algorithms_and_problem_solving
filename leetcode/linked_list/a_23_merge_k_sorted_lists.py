# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        h = []
        for lst in lists:
            if lst:
                curr = lst
                while curr:
                    h.append(curr.val * -1)
                    curr = curr.next
        if not h:
            return None
        heapq.heapify(h)
        head = ListNode(heapq.heappop(h) * -1)
        while h:
            vl = heapq.heappop(h)
            curr = ListNode(vl * -1, head)
            head = curr

        return head
