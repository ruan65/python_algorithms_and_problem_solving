# from collections import deque
# for _ in range(int(input())):
#     _, q = input(), deque(map(int, input().split()))
#
#     for n in reversed(sorted(q)):
#         if q[-1] == n:
#             q.pop()
#         elif q[0] == n:
#             q.popleft()
#         else:
#             print('No')
#             break
#     else:
#         print('Yes')

from collections import deque


for i in range(int(input())):
    _, n = input(), deque(map(int, input().split()))
    ans = True

    for j in range(len(n) - 1):
        if n[0] >= n[1]:
            n.popleft()
        elif n[-1] >= n[-2]:
            n.pop()
        else:
            ans = False
            break

    print('Yes' if ans else 'No')

# from collections import deque
# def pil(q):
#     if not q or len(q) == 1 or len(q) == 2:
#         return True
#     if q[0] >= q[1] and q[-1] >= q[-2]:
#         q.pop()
#         q.popleft()
#     elif q[0] >= q[1]:
#         q.popleft()
#     elif q[-1] >= q[-2]:
#         q.pop()
#     else:
#         return False
#     return pil(q)
#
# for _ in range(int(input())):
#     n = input()
#     d = deque(map(int, input().split()))
#     yes = pil(d)
#     print('Yes' if yes else 'No')


