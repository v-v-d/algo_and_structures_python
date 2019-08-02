"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


# Рекурсия
def get_sum_of_digits(num, sum_of_digits=0):
    sum_of_digits += num % 10
    num //= 10
    return get_sum_of_digits(num, sum_of_digits) if num else sum_of_digits


def get_num_from_user_and_get_sum(num_of_nums, i=1, sum_of_digits=0, max_sum_of_digits=0, max_sum_of_digits_num=None):
    num = int(input(f'Введите число №{i}: '))
    buffered_num = num
    sum_of_digits = get_sum_of_digits(num)
    if sum_of_digits > max_sum_of_digits:
        max_sum_of_digits = sum_of_digits
        max_sum_of_digits_num = buffered_num
    num_of_nums -= 1
    if num_of_nums:
        return get_num_from_user_and_get_sum(num_of_nums, i+1, sum_of_digits, max_sum_of_digits, max_sum_of_digits_num)
    else:
        return f'Число с максимальной суммой цифр: {max_sum_of_digits_num}, сумма цифр: {max_sum_of_digits}'


try:
    num_of_nums = int(input('Сколько чисел хотите ввести?: '))

    print(get_num_from_user_and_get_sum(num_of_nums))

except ValueError:
    print('Необходимо вводить целые числа')


# Цикл
try:
    num_of_nums = int(input('Сколько чисел хотите ввести?: '))

    max_sum_of_digits = 0
    max_sum_of_digits_num = None
    for i in range(num_of_nums):
        num = int(input(f'Введите число №{i + 1}: '))
        buffered_num = num
        sum_of_digits = 0
        while num:
            sum_of_digits += num % 10
            num //= 10
        if sum_of_digits > max_sum_of_digits:
            max_sum_of_digits = sum_of_digits
            max_sum_of_digits_num = buffered_num

    print(f'Число с максимальной суммой цифр: {max_sum_of_digits_num}, сумма цифр: {max_sum_of_digits}')
except ValueError:
    print('Необходимо вводить целые числа')
