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


# Применил метод .count() вместо генератора и последующего взятия его длины
def get_most_often_num_in_list_2(lst):
    checked_nums = []
    max_num_qty = 0
    most_often_num = lst[0]
    for num in lst:
        if num not in checked_nums:
            checked_nums.append(num)
            num_qty = lst.count(num)
            if num_qty > max_num_qty:
                max_num_qty = num_qty
                most_often_num = num
    return most_often_num


def main():
    get_ascii_table_recursively(32, 32 + 10)
    get_ascii_table_circle(32, 127, 10)

    lst = [random.randint(-10, 10) for _ in range(20)]
    get_most_often_num_in_list_1(lst)
    get_most_often_num_in_list_2(lst)


print(timeit.timeit('get_most_often_num_in_list_1(lst)',
                    setup='from __main__ import get_most_often_num_in_list_1, lst',
                    number=1000))

print(timeit.timeit('get_most_often_num_in_list_2(lst)',
                    setup='from __main__ import get_most_often_num_in_list_2, lst',
                    number=1000))

print(timeit.timeit('get_ascii_table_recursively(32, 32 + 10)',
                    setup='from __main__ import get_ascii_table_recursively',
                    number=1000))

print(timeit.timeit('get_ascii_table_circle(32, 127, 10)',
                    setup='from __main__ import get_ascii_table_circle',
                    number=1000))

cProfile.run('main()')


# результаты работы функции timeit:
# get_most_often_num_in_list_1 без использованиея метода .count():
# 0.021129100000000012
# get_most_often_num_in_list_2 с использованием метода .count():
# 0.009946699999999975
# Видно, что использование метода .count() дает прирост в скорости работы примерно в 2 раза. Видимо, это из-за того,
# что в данной реализации не создается список для подсчета элементов (проверил - это не так, не знаю из-за чего прирост.
# Может, встроенный метод работает быстрее самописных алгоритмов?)
#
# get_ascii_table_recursively с рекурсией:
# 0.1495039
# get_ascii_table_circle с циклом:
# 0.15628540000000002
# Тут результат удивил. В данной реализации рекурсия работает примерно с такой же скоростью, как и цикл
#
# Результат работы профилировщика cProfile:
# Все по нулям, видимо, оптимизировать ничего не надо
#
# 419 function calls (410 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      10/1    0.000    0.000    0.000    0.000 1.py:12(get_ascii_table_recursively)
#        10    0.000    0.000    0.000    0.000 1.py:22(get_ascii_string)
#         1    0.000    0.000    0.000    0.000 1.py:29(get_ascii_table_circle)
#         1    0.000    0.000    0.000    0.000 1.py:34(get_most_often_num_in_list_1)
#        12    0.000    0.000    0.000    0.000 1.py:41(<listcomp>)
#         1    0.000    0.000    0.000    0.000 1.py:49(get_most_often_num_in_list_2)
#         1    0.000    0.000    0.000    0.000 1.py:63(main)
#         1    0.000    0.000    0.000    0.000 1.py:67(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:218(randint)
#        20    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#       192    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        20    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        12    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        39    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# Сложность функций:
# get_ascii_table_recursively - сама рекурсия зависит от кол-ва элементов + цикл с функцией range() также зависит от
# кол-ва элементов, следовательно сложность данного алгоритма O(n^2)

# get_ascii_table_circle - данная функция вызывает в цикле функцию get_ascii_string, внутри которой есть цикл. Все эти
# циклы зависят от кол-ва элементов => сложность O(n^2)

# get_most_often_num_in_list_1 - внутри функции цикл с перебором элементов списка. Внутри цикла генератором создается
# список также перебором элементов исходного списка => сложность O(n^2)

# get_most_often_num_in_list_2 - Также, как и в случае с прошлой функцией, но вместо генератора списка используется
# метод count(), который в цикле перебирает список и возвращет кол-во элементов => сложность O(n^2)
