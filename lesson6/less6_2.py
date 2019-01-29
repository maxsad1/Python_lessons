import re

text = 'Hello #twitter!'

code = r'#(\w+)'

regexp = re.compile(code)

match = regexp.match(text)
print(match)

matches = regexp.findall(text)
print(matches)

matches = regexp.finditer(text)
for m in matches:
    print(m.group(0), m.group(1), m.start(), m.end())

