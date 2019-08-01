"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


# Рекурсия
def get_num_of_evens_and_odds(num, evens=0, odds=0):
    if (num % 10) % 2 == 0:
        evens += 1
    else:
        odds += 1
    num //= 10
    if num:
        return get_num_of_evens_and_odds(num, evens, odds)
    return f'Кол-во четных цифр: {evens}, кол-во нечетных: {odds}'


try:
    num = int(input('Введите натуральное число: '))

    print(get_num_of_evens_and_odds(num)) if num > 0 else print('Ошибка! Ноль - ненатуральное число')
except ValueError:
    print('Ошибка! Необходимо ввести натуральное число')


# Цикл
try:
    num = int(input('Введите натуральное число: '))

    if num > 0:
        num_of_evens = 0
        num_of_odds = 0

        while num:
            if (num % 10) % 2 == 0:
                num_of_evens += 1
            else:
                num_of_odds += 1
            num //= 10
        print(f'Кол-во четных цифр: {num_of_evens}')
        print(f'Кол-во нечетных цифр: {num_of_odds}')

    else:
        print('Ошибка! Ноль - ненатуральное число')
except ValueError:
    print('Ошибка! Необходимо ввести натуральное число')
