def substrCount(n, s):
    count = 0
    for i in range(1, len(s)):
        b = i - 1
        while b >= 0:
            print(f'i: {s[i]} b: {s[b]}')
            if s[b] == s[i]:
                count += 1
                b -= 1
            else:
                break
        f, e = i - 1, i + 1
        if s[f] == s[i]:
            continue
        comp = s[f]
        while f >= 0 and e < len(s):
            print(f'i: {s[i]} f: {s[f]} e: {s[e]}')
            if s[f] == s[e] == comp:
                count += 1
                f -= 1
                e += 1
            else:
                break
    return count + n


if __name__ == '__main__':
    print(substrCount(7, 'abcbaba'))
