from itertools import product

n, md = map(int, input().split())
lsts = []
for _ in range(n):
    lsts.append(map(int, input().split()[1:]))

mx = 0

for cm in product(*lsts):
    mx = max(mx, sum(a * a for a in cm) % md)
print(mx)
