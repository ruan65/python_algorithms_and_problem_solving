from collections import deque

f_reader = open('input__.txt', 'r')

size = int(f_reader.readline())
pointers = []
data = {}
result = deque()
steps = 0

for i in range(size):
    line = f_reader.readline().strip().split(' ')
    ints = [int(i) for i in line]
    data[i] = ints[1:]
    arr_size = ints[0]
    steps += arr_size
    pointers.append(arr_size - 1)


def fill_tails():
    tls = deque()
    for j in range(size):
        ind = pointers[j]
        if ind < 0:
            tls.append(-1)
        else:
            tls.append(data[j][ind])
    return tls


for k in range(steps):
    tails = fill_tails()
    max_val = max(tails)
    index = tails.index(max_val)
    result.append(max_val)
    pointers[index] -= 1

result.reverse()
solution = ''.join(f'{str(e)} ' for e in result)
solution.strip()
f_writer = open('output.txt', 'w')
f_writer.write(solution)





