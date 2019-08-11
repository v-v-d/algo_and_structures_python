"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile


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


def get_ascii_table_circle(from_symbol, to_symbol, step):
    for i in range(from_symbol, to_symbol + 1, step):
        print(get_ascii_string(i, i + step))


def main():
    get_ascii_table_recursively(32, 32 + 10)
    get_ascii_table_circle(32, 127, 10)


LAST_ASCII_NUM = 127
STEP = 10

print(timeit.timeit('get_ascii_table_recursively(32, 32 + 10)',
                    setup='from __main__ import get_ascii_table_recursively',
                    number=1000))

print(timeit.timeit('get_ascii_table_circle(32, 127, 10)',
                    setup='from __main__ import get_ascii_table_circle',
                    number=1000))

# результаты работы функции timeit:
# Рекурсия:
# 0.1495039
# Цикл:
# 0.15628540000000002

cProfile.run('main()')

# 317 function calls (308 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      10/1    0.000    0.000    0.000    0.000 1.py:11(get_ascii_table_recursively)
#        10    0.000    0.000    0.000    0.000 1.py:21(get_ascii_string)
#         1    0.000    0.000    0.000    0.000 1.py:28(get_ascii_table_circle)
#         1    0.000    0.000    0.000    0.000 1.py:33(main)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        40    0.000    0.000    0.000    0.000 cp1251.py:18(encode)
#        40    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
#       192    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        20    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
