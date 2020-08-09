import re
pt = re.compile(r'^(<[a-zA-Z])[\w._\-]*@[\w._\-]+\.[a-zA-Z]{1,3}>$')
m = re.match(pt, '<is_som@radom.stuff>')
if m:
    print(m.group())