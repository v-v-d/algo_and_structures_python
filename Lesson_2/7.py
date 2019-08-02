"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


# Рекурсия
def prove_equality(num, result=0):
    result += num
    if num != 0:
        return prove_equality(num - 1, result)
    return result


try:
    num = int(input('Введите число: '))
    check = num * (num + 1) / 2

    result = prove_equality(num)

    print('Равенство выполняется') if result == check else print('Равенство не выполняется')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')


# Цикл
try:
    num = int(input('Введите число: '))
    check = num * (num + 1) / 2

    result = 0
    for i in range(num):
        result += i + 1

    print('Равенство выполняется') if result == check else print('Равенство не выполняется')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')
