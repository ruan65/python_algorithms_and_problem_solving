# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]

        nd = head
        while nd.next:
            arr.append(nd.next)
            nd = nd.next
        mid = len(arr) // 2
        return arr[mid]
