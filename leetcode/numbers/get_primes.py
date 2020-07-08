from timeit import default_timer as timer

def get_primes(n: int) -> [int]:
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out

# def get_primes(n: int) -> [int]:
#     out = list()
#     sieve = set()
#     for p in range(2, n + 1):
#         if p not in sieve:
#             out.append(p)
#             for i in range(p, n + 1, p):
#                 sieve.add(i)
#     return out


if __name__ == '__main__':
    st = timer()
    print(len(get_primes(10000000)))
    print(f'elapsed: {timer() - st}')
