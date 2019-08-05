"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


# Рекурсия
def get_reverse_number(num, reverse_number=''):
    reverse_number += str(num % 10)
    num //= 10
    if num:
        return get_reverse_number(num, reverse_number)
    return reverse_number


try:
    num = int(input('Введите число: '))
    print(f'Обратное число: {print(get_reverse_number(num))}')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')


# Цикл
try:
    num = int(input('Введите число: '))

    reverse_num = ''
    while num:
        reverse_num += str(num % 10)
        num //= 10

    print(f'Обратное число: {reverse_num}')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')
