"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
import timeit


def get_median(lst):
    left, middle, right = [], [], []
    pivot = len(lst) // 2

    for el in lst:
        if el < lst[pivot]:
            left.append(el)
        elif el > lst[pivot]:
            right.append(el)
        else:
            middle.append(el)

    if lst == left + middle + right:
        # print(left + middle + right)
        return lst[pivot]
    else:
        return get_median(left + middle + right)


if __name__ == '__main__':
    m = random.randint(2, 20)

    random_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

    print(random_list)
    median = get_median(random_list)
    print(f'Медиана списка: {median}')

    print(timeit.timeit('get_median(random_list)',
                        setup='from __main__ import get_median, m, random_list',
                        number=1000))
