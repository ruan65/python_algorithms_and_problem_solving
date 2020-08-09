import re
pt_and = re.compile(r'(?<=\s)&&(?=\s)')
pt_or = re.compile(r'(?<=\s)\|\|(?=\s)')
for _ in range(int(input())):
    print(re.sub(pt_or, 'or', re.sub(pt_and, 'and', input())))
