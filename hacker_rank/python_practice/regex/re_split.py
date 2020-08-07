import re

inp = 'eabaabaabaabaae'
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
patt = re.compile(r'(?<=[' + c + r'])[' + v + ']{2,}(?=[' + c + '])', flags=re.I)
matches = re.findall(patt, inp)
print(-1) if not matches else print(*map(lambda w: w, matches), sep='\n')
