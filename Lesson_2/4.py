"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


# Рекурсия
def get_sum_of_series(num_of_elements, num=1, summ=0):
    summ += num
    num /= -2
    num_of_elements -= 1
    if num_of_elements:
        return get_sum_of_series(num_of_elements, num, summ)
    return summ


try:
    num_of_elements = int(input('Введите кол-во элементов: '))

    if num_of_elements > 0:
        print(f'Сумма {num_of_elements} элементов ряда: {get_sum_of_series(num_of_elements)}')
    else:
        print('Ошибка! Необходимо ввести положительное целое число больше 0')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')


# Цикл
try:
    num_of_elements = int(input('Введите кол-во элементов: '))

    if num_of_elements > 0:
        num = 1
        summ = 0
        for _ in range(num_of_elements):
            summ += num
            num /= -2

        print(f'Сумма {num_of_elements} элементов ряда: {summ}')
    else:
        print('Ошибка! Необходимо ввести положительное целое число больше 0')
except ValueError:
    print('Ошибка! Необходимо ввести целое число')
