"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
import random

rows = 5
cols = 4

matrix = [[random.randint(-50, 50) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(row)

print()

for row in range(rows):
    row_sum = 0
    for col in range(cols):
        row_sum += matrix[row][col]
    matrix[row].append(row_sum)

# Красивый вывод
for i, row in enumerate(matrix):
    output_str = ''
    for j, col in enumerate(row):
        output_str += f'{matrix[i][j]:>3} '
    print(output_str)
