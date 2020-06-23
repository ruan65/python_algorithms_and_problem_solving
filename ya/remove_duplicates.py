import sys

count = int(sys.stdin.readline().strip())


def print_unique(n):
    if n == 0:
        return

    curr = int(sys.stdin.readline().strip())
    last = curr
    print(curr)

    steps = 0

    while steps < count - 1:
        curr = int(sys.stdin.readline().strip())

        if curr != last:
            print(curr)
            last = curr

        steps += 1


print_unique(count)
