import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHaHamHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
pat
mat
bat
sat
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*')
# pattern = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'\s[^b]at')
# pattern = re.compile(r'[\da-zA-Z.-]+@[a-zA-Z-]+\.[a-z]+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)
#
# for m in matches:
#     print(m.group(3))

# with open('data.txt', 'r') as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#     for m in matches:
#         print(m)



