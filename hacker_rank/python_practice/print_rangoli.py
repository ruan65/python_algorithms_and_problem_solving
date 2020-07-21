def print_rangoli(size):
    a = ord('a')
    for i in range(-size + 1, size):
        w = ''
        for j in range(abs(i) + 1, size):
            w += '-' + chr(a + j)
        print((w[::-1] + chr(a + abs(i)) + w).center(4*size - 3, '-'))


if __name__ == '__main__':
    # n = int(input())
    print_rangoli(5)
    # print(wing(98, 2))