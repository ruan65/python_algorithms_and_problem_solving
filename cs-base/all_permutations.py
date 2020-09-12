from math import factorial

count = 0


def all_array_perm(arr: [], ch=[], out=[]) -> [[]]:
    global count
    count += 1
    if not arr:
        out.append(ch[:])
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        ch.append(arr[i])
        all_array_perm(new_arr, ch, out)
        ch.pop()
    return out


# def all_array_perm(inpt: []) -> [[]]:
#     out = []
#
#     def perm(arr: [], nums: []):
#         global count
#         count += 1
#         if not nums:
#             out.append(arr)
#             return
#         for i in range(len(nums)):
#             perm(arr + [nums[i]], nums[:i] + nums[i + 1:])
#
#     perm([], inpt)
#     return out


if __name__ == '__main__':
    inp = [1, 2, 3, 4, 5]
    prm = all_array_perm(inp)

    print(prm)

    print(f'is factorial: {len(inp)} {len(prm)} {factorial(len(inp)) == len(prm)}')

    print(count)
