"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit


def bubble_sort(lst):
    sorted_list = lst.copy()
    for _ in range(len(sorted_list)):
        is_already_sorted = True
        for i, el in enumerate(sorted_list):
            if i != len(sorted_list) - 1 and el < sorted_list[i + 1]:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                is_already_sorted = False
        if is_already_sorted:
            return sorted_list
    return sorted_list


if __name__ == '__main__':
    random_list_1 = [random.randint(-100, 100) for _ in range(27)]
    random_list_2 = [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    random_list_3 = [26, 27, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    print('На входе рандомный список:')
    print(random_list_1)
    print(bubble_sort(random_list_1))
    print(timeit.timeit('bubble_sort(random_list_1)',
                        setup='from __main__ import bubble_sort, random_list_1',
                        number=1000))

    print('На входе отсортированный список:')
    print(random_list_2)
    print(bubble_sort(random_list_2))
    print(timeit.timeit('bubble_sort(random_list_2)',
                        setup='from __main__ import bubble_sort, random_list_2',
                        number=1000))

    print('На входе список, в котором надо сделать одну замену:')
    print(random_list_3)
    print(bubble_sort(random_list_3))
    print(timeit.timeit('bubble_sort(random_list_3)',
                        setup='from __main__ import bubble_sort, random_list_3',
                        number=1000))
