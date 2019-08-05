"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


# Рекурсия
def get_calc():
    operator = input('Введите оператор или 0, чтобы выйти: ')
    if operator == '0':
        exit(0)

    try:
        if operator in ('/', ':', '*', '+', '-'):
            num1 = float(input('Введите первое число: '))
            num2 = float(input('Введите второе число: '))

            if operator in ('/', ':'):
                print(f'Результат деления: {num1 / num2}') if num2 != 0 else print('Ошибка! Делить на 0 нельзя')

            if operator == '*':
                print(f'Результат умножения: {num1 * num2}')

            if operator == '+':
                print(f'Результат сложения: {num1 + num2}')

            if operator == '-':
                print(f'Результат вычитания: {num1 - num2}')
        else:
            print('Вы ввели некорректный оператор')
    except ValueError:
        print('Необходимо ввести число. Разделитель - точка')
    return get_calc()


get_calc()

# Цикл
while True:
    operator = input('Введите оператор или 0, чтобы выйти: ')
    if operator == '0':
        break

    try:
        if operator in ('/', ':', '*', '+', '-'):
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))

            if operator in ('/', ':'):
                print(f'Результат деления: {num_1 / num_2}') if num_2 != 0 else print('Ошибка! Делить на 0 нельзя')

            if operator == '*':
                print(f'Результат умножения: {num_1 * num_2}')

            if operator == '+':
                print(f'Результат сложения: {num_1 + num_2}')

            if operator == '-':
                print(f'Результат вычитания: {num_1 - num_2}')
        else:
            print('Вы ввели некорректный оператор')
    except ValueError:
        print('Необходимо ввести число. Разделитель - точка')
