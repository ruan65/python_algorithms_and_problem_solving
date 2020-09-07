def find_parent(v, arr):
    while v != arr[v]:
        v = arr[v]
    return v


def join_sets(a, b, djs, count):
    if a != b:
        djs[b] = a
        count[a] += count[b]
        count[b] = 0
    return djs, count


def componentsInGraph(gb):
    disjoint_sets = [i for i in range(len(gb) * 2)]
    count = [1 for _ in range(len(gb) * 2)]
    for a, b in gb:
        pa = find_parent(a - 1, disjoint_sets)
        pb = find_parent(b - 1, disjoint_sets)
        disjoint_sets, count = join_sets(pa, pb, disjoint_sets, count)
    count = [v for v in count if v > 1]
    return min(count), max(count)
