import sys

sys.setrecursionlimit(10 ** 4)


# def minimumBribes(qq):
#     c = 0
#
#     def move_mx(q):
#         nonlocal c
#         if len(q) == 1:
#             return
#         mxi = q.index(max(q))
#         if len(q) - 1 - mxi > 2:
#             c = -1
#             return
#         elif mxi == len(q) - 1:
#             move_mx(q[:-1])
#
#         else:
#             c += len(q) - 1 - mxi
#             move_mx(q[:mxi] + q[mxi + 1:])
#
#     move_mx(qq)
#     print(c if c > -1 else 'Too chaotic')

def minimumBribes(q):
    count = 0

    def cd(arr):
        nonlocal count
        if len(arr) < 2:
            return
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                diff = arr[i] - arr[i + 1]
                count += diff
                if diff > 2:
                    count = -1
                    return
                cd(arr[:i])
                break

    cd(q)
    print(count if count > -1 else 'Too chaotic')


if __name__ == '__main__':
    minimumBribes(list(map(int, '1 2 5 3 7 8 6 4'.split())))
    minimumBribes([4, 1, 2, 3])
    # print(arr_data)
