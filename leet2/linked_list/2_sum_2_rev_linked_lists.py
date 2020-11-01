class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rev_list_to_num(l):
    n, k = 0, 1
    while l:
        n += l.val * k
        k *= 10
        l = l.next
    return n


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         n1, n2 = rev_list_to_num(l1), rev_list_to_num(l2)
#         s = str(n1 + n2)[::-1]
#         res = ListNode(int(s[0]))
#         if len(s) == 1:
#             return res
#         curr = res
#         for d in s[1:]:
#             curr.next = ListNode(int(d))
#             curr = curr.next
#         return res


def to_int(nd: ListNode) -> int:
    return nd.val + 10 * to_int(nd.next) if nd else 0


def to_list(n: int) -> ListNode:
    rout = ListNode(n % 10)
    if n > 9:
        rout.next = to_list(n // 10)
    return rout


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return to_list(to_int(l1) + to_int(l2))


if __name__ == '__main__':
    lst = ListNode(1)
    lst.next = ListNode(2)
    lst.next.next = ListNode(3)

    print(rev_list_to_num(lst))
    print(to_int(lst))

    print(to_int(Solution().addTwoNumbers(l1=lst, l2=lst)))
