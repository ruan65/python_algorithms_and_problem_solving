class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         res = None
#         while head:
#             res = ListNode(head.val, res)
#             head = head.next
#         return res

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev(curr, prev=None):
            if not curr:
                return prev
            cnext = curr.next
            curr.next = prev
            return rev(cnext, curr)
        return rev(head)


if __name__ == '__main__':
    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    while n1:
        print(n1.val, end='->')
        n1 = n1.next

    n4 = ListNode(val=4)
    n3 = ListNode(val=3, next=n4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    rev = Solution().reverseList(head=n1)
    print('\nnext')
    while rev:
        print(rev.val, end='->')
        rev = rev.next
