def child_nodes(i):
    return (2 * i) + 1, (2 * i) + 2


def traversed(lst, i=0, d=0):
    if i >= len(lst):
        return
    l, r = child_nodes(i)
    traversed(lst, r, d=d + 1)
    print("   " * d + str(lst[i]))
    traversed(lst, l, d=d + 1)


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
    traversed(a)
