def complement_32(n):
    bs = bin(n)
    return '0b' + '1' * (32 - len(bs) + 2) + bs[2:]


if __name__ == '__main__':
    print(complement_32(4))