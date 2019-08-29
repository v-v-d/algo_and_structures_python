"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import random
import hashlib

n = random.randint(10, 50)
first_ascii_num = 97
last_ascii_num = 122

s = ''.join([chr(random.randint(first_ascii_num, last_ascii_num)) for _ in range(n)])

substrings = set()
for i in range(len(s)):
    for j in reversed(range(i + 1, len(s))):
        substrings.add(hashlib.sha256(s[i:j].encode('UTF-8')).hexdigest())

print(f'Количество различных подстрок в строке "{s}": {len(substrings)}')
