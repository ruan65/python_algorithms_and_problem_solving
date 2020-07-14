import sys
import heapq


def str_list_to_int_list(str_list):
    i_ = 0
    while i_ < len(str_list):
        str_list[i_] = int(str_list[i_])
        i_ += 1
    return str_list


size = int(sys.stdin.readline().strip())
data = []


# for i in range(size):
#     line = sys.stdin.readline().strip().split(' ')
#     str_list_to_int_list(line)
#     data.extend(line[1:])

for i in range(size):
    line = sys.stdin.readline().strip().split(' ')
    str_list_to_int_list(line)
    data.extend(line[1:])

data.sort()

for n in data:
    print(str(n), end=' ')


