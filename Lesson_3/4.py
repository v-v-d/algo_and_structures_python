# 4.	Определить, какое число в массиве встречается чаще всего.
import random

lst = [random.randint(-10, 10) for _ in range(20)]

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

print(lst)
print(f'В данном списке чаще всего встречается число {most_often_num} ({max_num_qty} раз(a))')
