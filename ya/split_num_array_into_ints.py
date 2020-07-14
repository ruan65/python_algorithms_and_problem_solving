# def get_ranges((b, p), (z, d)):
#     if p is not None:
#         if d == 1: return (b, p)
#         b.append('%d-%d' % (p, z))
#         return (b, None)
#     else:
#         if d == 1: return (b, z)
#         b.append(str(z))
#         return (b, None)


def get_str_of_intervals(arr: []) -> str:
    if not arr:
        return ''
    breaks = []
    arr.sort()
    start = end = arr[0]
    for i in arr[1:]:
        diff = i - end
        if diff == 1:
            end = i
        else:
            breaks.append((start, end))
            start = end = i
    breaks.append((start, end))
    return ','.join(str(s) if s == e else f'{s}-{e}' for s, e in breaks)


print(get_str_of_intervals([1, 2, 8,9, 15]))
