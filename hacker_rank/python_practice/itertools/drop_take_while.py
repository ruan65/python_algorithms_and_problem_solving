import itertools as it

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 10, 20, 30]
names = ['andrey', 'liza']


def gr(n):
    return n < 10


print(*it.dropwhile(gr, numbers))
print(*it.takewhile(gr, numbers))
