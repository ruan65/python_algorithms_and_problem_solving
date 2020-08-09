import re
import itertools

s, k = 'aaadaa', 'e'
m = list(re.finditer(r'(?=(' + k + '))', s))

print((-1, -1)) if not list(m) else print(*map(lambda f: (f.start(), f.end() + len(k) - 1), m), sep='\n')
