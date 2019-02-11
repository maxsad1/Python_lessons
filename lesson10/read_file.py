chars = {}
with open(r'D:\MyDocs\python\homework\library_dir\library\Dubrovskij.txt', mode='r', encoding='utf-8') as f:
    for char in f.read():
        # sum_chars = chars.get(char, 0) + 1
        # chars[char] = sum_chars
        chars[char] = chars.setdefault(char, 0) + 1

print(chars)