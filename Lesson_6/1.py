"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from collections import Counter
import timeit
import random
from memory_profiler import profile


# @profile
def get_most_common_in_list_1(lst):
    checked_nums = []
    max_num_qty = 0
    most_common_num = lst[0]
    for num in lst:
        if num not in checked_nums:
            checked_nums.append(num)
            num_qty = len([el for el in lst if el == num])
            if num_qty > max_num_qty:
                max_num_qty = num_qty
                most_common_num = num
    return most_common_num


# @profile
def get_most_common_in_list_2(lst):
    return Counter(lst).most_common(1)[0][0]


# @profile
def get_most_common_in_list_3(lst):
    return max(set(lst), key=lst.count)


if __name__ == '__main__':
    lst = [random.randint(-100, 100) for _ in range(100000)]

    get_most_common_in_list_1(lst)
    get_most_common_in_list_2(lst)
    get_most_common_in_list_3(lst)

    # Результат работы функции profile модуля memory_profile:
    #
    # Line #    Mem usage    Increment   Line Contents
    # ================================================
    #     15     15.3 MiB     15.3 MiB   @profile
    #     16                             def get_most_common_in_list_1(lst):
    #     17     15.3 MiB      0.0 MiB       checked_nums = []
    #     18     15.3 MiB      0.0 MiB       max_num_qty = 0
    #     19     15.3 MiB      0.0 MiB       most_common_num = lst[0]
    #     20     15.4 MiB      0.0 MiB       for num in lst:
    #     21     15.4 MiB      0.0 MiB           if num not in checked_nums:
    #     22     15.4 MiB      0.0 MiB               checked_nums.append(num)
    #     23     15.4 MiB      0.0 MiB               num_qty = len([el for el in lst if el == num])
    #     24     15.4 MiB      0.0 MiB               if num_qty > max_num_qty:
    #     25     15.3 MiB      0.0 MiB                   max_num_qty = num_qty
    #     26     15.3 MiB      0.0 MiB                   most_common_num = num
    #     27     15.2 MiB      0.0 MiB       return most_common_num

    # get_most_common_in_list_2(lst)

    # Line #    Mem usage    Increment   Line Contents
    # ================================================
    #     30     15.2 MiB     15.2 MiB   @profile
    #     31                             def get_most_common_in_list_2(lst):
    #     32     15.2 MiB      0.0 MiB       return Counter(lst).most_common(1)[0][0]

    # get_most_common_in_list_3(lst)

    # Line #    Mem usage    Increment   Line Contents
    # ================================================
    #     35     15.2 MiB     15.2 MiB   @profile
    #     36                             def get_most_common_in_list_3(lst):
    #     37     15.2 MiB      0.0 MiB       return max(set(lst), key=lst.count)

    # Результат работы метода timeit модуля timeit.
    # lst = [random.randint(-100, 100) for _ in range(1000)]
    #
    # print(timeit.timeit('get_most_common_in_list_1(lst)',
    #                     setup='from __main__ import get_most_common_in_list_1, lst',
    #                     number=1000))

    # 10.0703481

    # print(timeit.timeit('get_most_common_in_list_2(lst)',
    #                     setup='from __main__ import get_most_common_in_list_2, lst',
    #                     number=1000))

    # 0.09350539999999974

    # print(timeit.timeit('get_most_common_in_list_3(lst)',
    #                     setup='from __main__ import get_most_common_in_list_3, lst',
    #                     number=1000))

    # 4.170727500000002

    # Выводы:
    # По результатам работы memory_profile видно, что первая функция требует больше памяти, чем остальные 2. Особенно
    # это заметно на строчках 20-24, где потребление памяти начинает расти. Это место в функции требует доработки.
    # Остальные 2 функции потребляют одинаковое количество памяти.
    # Замер по времени отрабатывания функций хоть был и не нужен по заданию, но мне стало интересно какой вариант
    # работает быстрее. И вот тут видно, что тип данных Counter модуля collections выигрывает по всем параметрам
    # стандартные и самописные функции при поиске самого частого элемента в списке.
