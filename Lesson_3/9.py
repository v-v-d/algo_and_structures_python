# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

rows = 5
cols = 5

matrix = [[random.randint(-50, 50) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(row)

print()

min_col_nums = []
for row in matrix:
    min_col_num = float('inf')
    for col in row:
        if col < min_col_num:
            min_col_num = col
    min_col_nums.append(min_col_num)

max_in_min_col_nums = -float('inf')
for num in min_col_nums:
    if num > max_in_min_col_nums:
        max_in_min_col_nums = num

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_in_min_col_nums}')
