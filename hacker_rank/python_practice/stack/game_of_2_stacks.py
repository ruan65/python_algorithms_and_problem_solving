def two_stacks(x, a, b):
    sm, sma, mx = 0, 0, 0

    for i, n in enumerate(a):
        sma += n
        if sma > x:
            break
        sm = sma
        count, curb = i + 1, list(b)
        while sm <= x and curb:
            mx = max(mx, count)
            nb = curb.pop(0)
            sm += nb
            count += 1
    sma = 0
    for i, n in enumerate(b):
        sma += n
        if sma > x:
            break
        sm = sma
        count, curb = i + 1, list(a)
        while sm <= x and curb:
            mx = max(mx, count)
            nb = curb.pop(0)
            sm += nb
            count += 1

    return mx


if __name__ == '__main__':
    a = list(map(int, '11 6 1 13 14 7 8 10 3 17 7 18 6 4 5 13 17 4 16 9 17 16 12 6 7'.split()))
    b = list(map(int, '10 15 13 17 10 7 0 16 8 13 11 8 14 13'.split()))
    print(two_stacks(5, a, b))
