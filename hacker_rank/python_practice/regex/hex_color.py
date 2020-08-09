import re

pt = re.compile(r'(?<!^)#(?:[\da-fA-F]{3}){1,2}')

for _ in range(int(input())):
    it = re.finditer(pt, input())
    for i in it:
        print(i.group())