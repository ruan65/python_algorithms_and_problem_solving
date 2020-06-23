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

f_reader.close()


def fill_tails():
    tls = []
    for j in range(size):
        ind = pointers[j]
        if ind < 0:
            tls.append(-1)
        else:
            tls.append(data[j][ind])
    return tls


def find_max_val_and_index(arr):
    mv = -1
    mi = -1
    for elm in range(len(arr)):
        if arr[elm] > mv:
            mv = arr[elm]
            mi = elm
    return mi, mv


for k in range(steps):
    tails = fill_tails()
    index, max_val = find_max_val_and_index(tails)
    result.appendleft(max_val)
    pointers[index] -= 1

solution = ''.join(f'{str(e)} ' for e in result)
solution.strip()
f_writer = open('output.txt', 'w')
f_writer.write(solution)
f_writer.close()
