# gen = (x * x for x in range(5))
#
# print('gen 1')
# for n in gen:
#     print(n)
#
# print('gen 1')
# for n in gen:
#     print(n)


def generator_int(k):
    for i in range(k):
        yield k


g = generator_int(3)
for e in g:
    print(f' gen:{e}')

print('*********')

for e in g:
    print(f' gen:{e}')