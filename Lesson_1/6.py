# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

try:
    letter_pos = int(input('Введите номер буквы в диапазоне 97 - 122: '))

    symbol_range = range(ord('a'), ord('z') + 1)
    print(chr(letter_pos)) if letter_pos in symbol_range else print('Необходимо ввести число в диапазоне 97 - 122')
except ValueError:
    print('Необходимо ввести целое число')
