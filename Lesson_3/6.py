"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

lst = [random.randint(-50, 50) for _ in range(20)]

min_num, max_num = lst[0], lst[0]
min_idx, max_idx = 0, 0
for i, num in enumerate(lst):
    if num > max_num:
        max_num = num
        max_idx = i
    elif num < min_num:
        min_num = num
        min_idx = i

nums_between_idxs = lst[min_idx + 1:max_idx] if min_idx < max_idx else lst[max_idx + 1:min_idx]

sum_between_idxs = 0
for num in nums_between_idxs:
    sum_between_idxs += num

print(lst)
print(nums_between_idxs)
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum_between_idxs}')
