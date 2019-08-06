#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random

lst = [random.randint(-50, 50) for i in range(20)]

max_negative_num = -float('inf')
max_negative_num_index = None
for i, num in enumerate(lst):
    if max_negative_num < num < 0:
        max_negative_num = num
        max_negative_num_index = i

print(lst)
print(f'Максимальный отрицательный элемент в списке: {max_negative_num}, его индекс: {max_negative_num_index}')
