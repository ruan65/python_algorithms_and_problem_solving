import bisect

if __name__ == '__main__':
    a = [15, 23, 23]
    bisect.insort(a, 27)
    print(bisect.bisect_right(a, 23))
