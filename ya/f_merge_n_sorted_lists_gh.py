import sys

counter = [0 for _ in range(101)]
lines = int(sys.stdin.readline().strip())

for i in range(int(lines)):
    s = sys.stdin.readline().strip()

    for index, value in enumerate(s.split(' ')):
        if index == 0:
            continue
        counter[int(value)] += 1

for n in range(101):
    if counter[n]:
        print(' '.join([str(n)] * counter[n]), end=' ')

