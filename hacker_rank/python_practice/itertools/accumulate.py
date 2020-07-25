import itertools as it
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 10, 20, 30]
names = ['andrey', 'liza']

print(*it.accumulate(numbers))
print(*it.accumulate(numbers, lambda curr, prev: curr*prev))
print(*it.accumulate(numbers, operator.mul))
print(*it.accumulate(range(10)))