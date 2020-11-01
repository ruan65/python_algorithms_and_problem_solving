class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_to_int(h: ListNode) -> int:
    res = 0
    while h:
        print(h.val)
        res = 2 * res + h.val
        h = h.next
    return res


if __name__ == '__main__':
    head = ListNode(1, ListNode(1, ListNode(0, ListNode(1))))
    print(convert_to_int(head))
