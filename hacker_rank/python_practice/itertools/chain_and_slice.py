import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['andrey', 'liza']

print(*itertools.chain(letters, numbers, names))
print(*itertools.islice(itertools.chain(letters, numbers, names), 0, len(letters)))

with open('sample.log', 'r') as f:
    header = itertools.islice(f, 4)
    print(*header)