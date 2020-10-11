def largest_rect(h):
    mx = 0

    def div_conq(k):
        nonlocal mx
        if not k:
            return
        mx = max(mx, min(k) * len(k))
        i = k.index(min(k))
        l, r = k[0:i], k[i+1:]
        if len(l) > 1:
            div_conq(l)
        if len(r) > 1:
            div_conq(r)
    div_conq(h)
    return mx


if __name__ == '__main__':
    print(largest_rect([3, 2, 5, 6, 1, 4, 4]))
