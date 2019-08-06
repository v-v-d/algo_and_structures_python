#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

lst = [random.randint(-10, 10) for i in range(20)]

print(lst)

min_index, max_index = 0, 0
min_num, max_num = lst[0], lst[0]
for i, num in enumerate(lst):
    if num < min_num:
        min_num = num
        min_index = i
    elif num > max_num:
        max_num = num
        max_index = i
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

print(lst)
