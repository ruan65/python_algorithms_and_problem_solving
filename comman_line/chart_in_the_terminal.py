#!/usr/bin/env python
import math
import random
import sys

columns = 15
data = [random.randint(1, 100) for i in range(columns)]
minimum = min(data)
maximum = max(data)
chart = []
rows = 10

# chart structure
for row in range(rows):
    chart.append([])
    chart[row].append(math.ceil(row * maximum / rows))
    for d in data:
        chart[row].append('   ')

# fill values

for r_id, r in enumerate(chart):
    for c_id, col in enumerate(data, start=1):
        if col > r[0]:
            chart[r_id][c_id] = ' _ '


def print_chart(ch: [[]]):
    prt = sys.stdout.write
    ch.reverse()
    for rw in ch:
        for cl in rw:
            # if ch[r][0] < 10:
            # prt(' ')
            prt(f'{str(cl).rjust(3)} ')
        prt('\n')

    prt('    ')
    for vl in data:
        prt(f'{str(vl).ljust(4)}')


print(data)

print(f'min: {minimum} max: {maximum}')
print(print_chart(chart))


# run
# while true; do clear && ./chart_in_the_terminal.py && sleep .5; done