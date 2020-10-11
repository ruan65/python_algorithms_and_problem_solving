def all_array_perm(inp: []) -> [[]]:
    out = []

    def perm(arr: [], els: []):
        if not els:
            out.append(arr)
            return
        for i in range(len(els)):
            perm(arr + [els[i]], els[0:i] + els[i + 1:])

    perm([], inp)
    return out


if __name__ == '__main__':
    inp = [1, 2, 3, 4, 5]
    prm = all_array_perm(inp)

    print(prm)
