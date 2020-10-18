def is_prime(p):
    if p == 2:
        return True
    if p == 1 or p % 2 == 0:
        return False
    for i in range(3, int(p ** .5) + 1, 2):
        if p % i == 0:
            return False
    return True


# def primality(n):
#     out = list()
#     sieve = [True] * (n + 1)
#     for p in range(2, n + 1):
#         if sieve[p]:
#             out.append(p)
#             for i in range(p, n + 1, p):
#                 sieve[i] = False
#     return('Prime' if out and out[-1] == n else 'Not prime')

if __name__ == '__main__':
    print(is_prime(1000000007))
