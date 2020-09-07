# def outer(some_fn):
#     def inner():
#         print('before some_fn')
#         return some_fn() + 1
#
#     return inner
#
#
# def foo():
#     return 100
#
#
# def baz():
#     return 200
#
#
# # decorated_foo = outer(foo)
# # decorated_baz = outer(baz)
# #
# # print(decorated_foo())
# # print(decorated_baz())
#
# print(foo())
#
# foo = outer(foo)

# print(foo())

def wrapper(f):
    def fun(l):
        return f([f'+91 {n[-10:-5]} {n[-5:]}' for n in l])

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
