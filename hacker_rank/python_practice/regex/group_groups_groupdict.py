import re
inp = '..123345678910111213141516171820212223'


pt = re.compile(r'([a-zA-Z0-9])\1')
m = re.search(pt, inp)
print(m)
print(m.group(1) if m else -1)
