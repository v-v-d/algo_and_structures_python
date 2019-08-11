"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit


# Рекурсия
def get_ascii_table_recursively(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f'{i} - {chr(i)} '
    # print(output_str)
    if to_symbol < LAST_ASCII_NUM:
        return get_ascii_table_recursively(from_symbol + STEP, to_symbol + STEP)


# Цикл
def get_ascii_string(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= LAST_ASCII_NUM:
            output_str += f'{i} - {chr(i)} '
    return output_str


LAST_ASCII_NUM = 127
STEP = 10

print('Рекурсия:')
print(timeit.timeit('get_ascii_table_recursively(32, 32 + 10)',
                    setup='from __main__ import get_ascii_table_recursively',
                    number=1000))

print('Цикл:')
print(timeit.timeit('for i in range(32, 127 + 1, 10): get_ascii_string(i, i + 10)',
                    setup='from __main__ import get_ascii_string',
                    number=1000))

# timeit показал незначительну разницу по времени выполнения
