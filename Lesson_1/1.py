# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

try:
    num = int(input('Введите трехзначное число: '))
    min_digits = 3
    max_digits = 3

    if min_digits <= len(str(num)) <= max_digits and abs(num) == num:
        digit_3 = num % 10
        num //= 10
        digit_2 = num % 10
        num //= 10
        digit_1 = num % 10

        print(f'Сумма всех цифр: {digit_1 + digit_2 + digit_3}')
        print(f'Произведение всех цифр: {digit_1 * digit_2 * digit_3}')
    else:
        print('Число должно быть положительным и трехзначным')

except ValueError:
    print('Необходимо ввести целое число')
