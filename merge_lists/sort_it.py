f_reader = open('input.txt', 'r')

size = int(f_reader.readline())
data = []

for i in range(size):
    line = f_reader.readline().strip().split(' ')
    ints = [int(i) for i in line]
    data.extend(ints[1:])

data.sort()


