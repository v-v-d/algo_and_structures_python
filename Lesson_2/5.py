"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


# Рекурсия
def get_ascii_table_recursively(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f'{i} - {chr(i)} '
    print(output_str)
    if to_symbol < LAST_ASCII_NUM:
        return get_ascii_table_recursively(from_symbol + STEP, to_symbol + STEP)


# Цикл
def get_ascii_string(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f'{i} - {chr(i)} '
    return output_str


first_ascii_num = 32
LAST_ASCII_NUM = 127
STEP = 10

print('Это вывод рекурсии:')
get_ascii_table_recursively(first_ascii_num, first_ascii_num + STEP)

print('Это вывод цикла:')
for i in range(first_ascii_num, LAST_ASCII_NUM + 1, STEP):
    print(get_ascii_string(i, i + STEP))
