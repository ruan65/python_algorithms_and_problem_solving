def three_sum(arr: [int]):
    d = {}
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] in d:
                d[arr[i] + arr[j]].append([i, j])
            else:
                d[arr[i] + arr[j]] = [[i, j]]
    print(d)
    for i, v in enumerate(arr):
        if -v in d:
            for p in d[-v]:
                if i not in p:
                    triple = (arr[p[0]], arr[p[1]], v)
                    res.append(triple)

    return res


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
