count = 0


def knapSack(capacity, w, v, n) -> int:
    def ks(i, cap) -> int:
        global count
        count += 1
        if i < 0 or cap <= 0:
            return 0
        elif w[i] > cap:
            return ks(i - 1, cap)
        else:
            opt1 = ks(i - 1, cap)
            opt2 = v[i] + ks(i - 1, cap - w[i])
            return max(opt1, opt2)

    return ks(n, capacity)


if __name__ == '__main__':
    count = 0
    cp = 8
    wt = [5, 4, 6, 3, 2, 1, 7]
    vl = [70, 45, 80, 35, 10, 5, 90]

    sack = knapSack(cp, wt, vl, len(wt) - 1)
    print(sack)
    print(count)
