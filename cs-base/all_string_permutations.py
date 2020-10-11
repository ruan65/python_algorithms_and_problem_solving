from math import factorial

count = 0


def all_str_perm(word: str) -> [str]:
    out = []
    inpt = list(word)

    def perm(arr: [], chars: []):
        if not chars:
            out.append(''.join(arr))
            return
        for i in range(len(chars)):
            perm(arr + [chars[i]], chars[:i] + chars[i + 1:])

    perm([], inpt)
    return out


if __name__ == '__main__':
    inp = 'abc'
    prm = all_str_perm(inp)

    print(prm)

    print(f'is factorial: {len(inp)} {len(prm)} {factorial(len(inp)) == len(prm)}')
