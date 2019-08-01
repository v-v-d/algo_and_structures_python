# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

try:
    num_1 = float(input('Введите число №1: '))
    num_2 = float(input('Введите число №2: '))
    num_3 = float(input('Введите число №3: '))

    if num_1 == num_2 == num_3:
        print('Числа одинаковые')
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        print('Два из трех чисел одинаковые')
    else:
        if num_2 < num_1 < num_3:
            print(num_1)
        elif num_1 < num_2 < num_3:
            print(num_2)
        else:
            print(num_3)
except ValueError:
    print('Необходимо ввести число, разделитель - точка')
