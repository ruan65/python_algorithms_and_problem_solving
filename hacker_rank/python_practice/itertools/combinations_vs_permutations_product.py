import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['andrey', 'liza']


print(*itertools.combinations(letters, 2))
print(*itertools.permutations(letters, 2))

print(*itertools.combinations(numbers, len(numbers)))
print(*itertools.permutations(numbers))

print(*itertools.combinations(names, 2))
print(*itertools.permutations(names, 2))

print(*itertools.product(numbers, repeat=5))
print(*itertools.product(names, repeat=3))
print(*itertools.combinations_with_replacement(names, 3))


