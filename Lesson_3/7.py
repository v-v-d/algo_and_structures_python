"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random

lst = [random.randint(-50, 50) for i in range(20)]

min_num_1, min_num_2 = lst[0], lst[0]
min_num_1_idx = 0
for i, num in enumerate(lst):
    if num < min_num_1:
        min_num_1 = num
        min_num_1_idx = i

lst_without_min_num_1 = lst[:min_num_1_idx] + lst[min_num_1_idx + 1:]

for num in lst_without_min_num_1:
    if num < min_num_2:
        min_num_2 = num

print(lst)
print(min_num_1, min_num_2)
