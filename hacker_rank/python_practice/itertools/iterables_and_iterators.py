import itertools as it
_, lst, k = input(), input().split(), int(input())

comb = list(it.combinations(lst, k))
fr = sum(1 for _ in filter(lambda l: 'a' in l, comb))
print(fr/len(comb))
