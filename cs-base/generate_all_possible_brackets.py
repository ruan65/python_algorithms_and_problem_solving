def gen_brackets(size):
    output = []

    def gen(o, c, n, res):
        if c == n:
            output.append(res)
            return
        if o < n:
            gen(o + 1, c, n, res + '(')
        if c < o:
            gen(o, c + 1, n, res + ')')

    gen(0, 0, size, '')
    return output


if __name__ == '__main__':
    print(gen_brackets(3))
