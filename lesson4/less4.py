f = open('file.txt', 'r', encoding='utf-8')
num = 0
for line in f:
    if line.startswith('#'):
        num += 1
f.close()
print('Comments string number:', num)

rows = []
with open('file.txt', 'r', encoding='utf-8') as f:
    num = 0
    for line in f:
        if line.startswith('#'):
            num += 1
        else:
            rows.append(line)
print('Comments string number:', num)
print('Strings number:', len(rows))

with open('file_out.txt', 'w', encoding='utf-8') as f:
    num = 0
    for line in rows:
        line = line.replace('\n', '').replace('\r', '')
        f.write(line + '\n')
        num += 1
        print(line, file=f)

print('Strings are written:', num)

with open('file_out.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

with open('file.txt', 'r', encoding='utf-8') as f_in, (
     open('file_out.txt', 'w', encoding='utf-8')) as f_out:
    for in_line in f_in:
        if not in_line.startswith('#'):
            out_line = in_line.replace('\n', '').replace('\r', '')
            f_out.write(out_line + '\n')

with open('file_out.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

