import itertools as it

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['andrey', 'liza']

selectors = [True, True, False, True]

print(*it.compress(letters, selectors))


# filter example

def odd(n):
    return n % 2 == 1


print(*filter(odd, numbers))
print(*it.filterfalse(odd, numbers))
