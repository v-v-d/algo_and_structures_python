"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


limit1 = input('Введите целое число, вещественное число или символ, который будет являться нижней границей предела: ')
limit2 = input('Введите целое число, вещественное число или символ, который будет являться верхней границей предела: ')

symbol_range = range(ord('a'), ord('z') + 1)

try:
    if is_int(limit1) and is_int(limit2):
        result = int(random.random() * (int(limit2) - int(limit1) + 1)) + int(limit1)
    elif is_float(limit1) and is_float(limit2):
        result = random.random() * (float(limit2) - float(limit1) + 1) + float(limit1)
    elif ord(limit1) in symbol_range and ord(limit2) in symbol_range:
        random_ascii_code = int(random.random() * (ord(limit2) - ord(limit1) + 1)) + ord(limit1)
        result = chr(random_ascii_code)
    print(result)
except NameError:
    print('Необходимо ввести целое число, вещественное число или символ в пределах a-z')
except TypeError:
    print('Символ должен быть в пределах a-z, разделителем вещественного числа должна быть точка')
