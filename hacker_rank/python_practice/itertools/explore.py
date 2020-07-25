import itertools as it

rp5 = it.repeat(5)
rp2 = it.repeat(2)

mp = map(pow, range(10), rp2)

print(*mp)

sm = it.starmap(pow, [(2, 3), (3, 3), (4, 3)])

s = 'a b c a d b z e o'.split()
# a_at = [i for i in range(len(s)) if s[i] == 'a']
# comb = list(it.combinations(range(len(s)), 4))
# cc = 0
# for cm in comb:
#     print(cm)
# print(cc / len(comb))
#
# print({1, 4}.intersection([1, 2, 3]))
#
# fr = reduce(lambda x, y: x + y, (1 for c in comb if set(a_at).intersection(c)))
# print(fr/len(comb))

comb = list(it.combinations(s, 4))
fr = list(filter(lambda l: 'a' in l, comb))
print(fr)
print(len(fr) / len(comb))
