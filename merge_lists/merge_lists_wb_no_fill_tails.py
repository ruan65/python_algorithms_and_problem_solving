from collections import deque

f_reader = open('input.txt', 'r')

size = int(f_reader.readline())
pointers = []
data = {}
result = deque()
steps = 0

for i in range(size):
    line = f_reader.readline().strip().split(' ')
    ints = [int(i) for i in line]
    arr_size = ints[0]
    data[i] = ints[1:] if arr_size > 0 else []
    steps += arr_size
    pointers.append(arr_size - 1)

def find_max_index():
    sample = []
    for y in range(size):
        ind = pointers[y]
        if ind < 0:
            sample.append(-1)
        else:
            sample.append(data[y][ind])
    mav = max(sample)
    indx = sample.index(mav)
    pointers[indx] -= 1
    return mav


for k in range(steps):
    current_max = find_max_index()
    result.appendleft(current_max)

solution = ''.join(f'{str(e)} ' for e in result)
f_writer = open('output.txt', 'w')
f_writer.write(solution)
