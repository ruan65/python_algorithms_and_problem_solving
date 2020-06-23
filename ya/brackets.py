import sys


def generate(seq, op, closed, size):
    if len(seq) == size * 2:
        print(seq)
        return

    if op < size:
        generate(seq + '(', op + 1, closed, size)

    if closed < op:
        generate(seq + ')', op, closed + 1, size)


def make_brackets(n):
    generate('', 0, 0, n)


count = int(sys.stdin.readline().strip())
make_brackets(count)
