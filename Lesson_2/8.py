"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


# Рекурсия
def count_of_digit_in_num(num, desired_digit, result=0):
    if num % 10 == desired_digit:
        result += 1
    num //= 10
    return count_of_digit_in_num(num, desired_digit, result) if num else result


def get_num_from_user(num_of_nums, num_of_num=1, result=0):
    num = int(input(f'Введите число №{num_of_num}: '))
    result += count_of_digit_in_num(num, desired_digit)
    num_of_nums -= 1
    return get_num_from_user(num_of_nums, num_of_num + 1,  result) if num_of_nums else result


try:
    num_of_nums = int(input('Сколько чисел хотите ввести?: '))

    while True:
        desired_digit = int(input('Введите искомую цифру: '))
        if desired_digit > 9:
            print('Ошибка! Необходимо ввести цифру в диапазоне 0-9')
        else:
            break

    result = get_num_from_user(num_of_nums)

    print(f'Цифра {desired_digit} встречается в данной последовательности чисел {result} раз')
except ValueError:
    print('Необходимо вводить целые числа')


# Цикл
try:
    num_of_nums = int(input('Сколько чисел хотите ввести?: '))

    while True:
        desired_digit = int(input('Введите искомую цифру: '))
        if desired_digit > 9:
            print('Ошибка! Необходимо ввести цифру в диапазоне 0-9')
        else:
            break

    result = 0
    for i in range(num_of_nums):
        num = int(input(f'Введите число №{i + 1}: '))
        while num:
            if num % 10 == desired_digit:
                result += 1
            num //= 10

    print(f'Цифра {desired_digit} встречается в данной последовательности чисел {result} раз')
except ValueError:
    print('Необходимо вводить целые числа')
