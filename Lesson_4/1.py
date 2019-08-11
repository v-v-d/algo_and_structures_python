"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile
import random


# Рекурсия
def get_ascii_table_recursively(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= 127:
            output_str += f'{i} - {chr(i)} '
    print(output_str)
    if to_symbol < 127:
        return get_ascii_table_recursively(from_symbol + 10, to_symbol + 10)


# Цикл
def get_ascii_string(from_symbol, to_symbol, output_str=''):
    for i in range(from_symbol, to_symbol):
        if i <= 127:
            output_str += f'{i} - {chr(i)} '
    return output_str


def get_ascii_table_circle(from_symbol, to_symbol, step):
    for i in range(from_symbol, to_symbol + 1, step):
        print(get_ascii_string(i, i + 10))


def main():
    get_ascii_table_recursively(32, 32 + 10)
    get_ascii_table_circle(32, 127, 10)


def get_most_often_num_in_list_1(lst):
    checked_nums = []
    max_num_qty = 0
    most_often_num = lst[0]
    for num in lst:
        if num not in checked_nums:
            checked_nums.append(num)
            num_qty = len([el for el in lst if el == num])
            if num_qty > max_num_qty:
                max_num_qty = num_qty
                most_often_num = num
    return most_often_num


def get_most_often_num_in_list_2(lst):
    checked_nums = []
    max_num_qty = 0
    most_often_num = lst[0]
    for num in lst:
        if num not in checked_nums:
            checked_nums.append(num)
            if lst.count(num) > max_num_qty:
                max_num_qty = lst.count(num)
                most_often_num = num
    return most_often_num


lst = [random.randint(-10, 10) for _ in range(20)]

print(timeit.timeit('get_most_often_num_in_list_1(lst)',
                    setup='from __main__ import get_most_often_num_in_list_1, lst',
                    number=1000))

print(timeit.timeit('get_most_often_num_in_list_2(lst)',
                    setup='from __main__ import get_most_often_num_in_list_2, lst',
                    number=1000))

# результаты работы функции timeit:
# get_most_often_num_in_list_1 без использованиея функции .count():
# 0.021129100000000012
# get_most_often_num_in_list_2 с использованием функции .count():
# 0.009946699999999975

print(timeit.timeit('get_ascii_table_recursively(32, 32 + 10)',
                    setup='from __main__ import get_ascii_table_recursively',
                    number=1000))

print(timeit.timeit('get_ascii_table_circle(32, 127, 10)',
                    setup='from __main__ import get_ascii_table_circle',
                    number=1000))

# результаты работы функции timeit:
# get_ascii_table_recursively с рекурсией:
# 0.1495039
# get_ascii_table_circle с циклом:
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
