"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

try:
    side_a = float(input('Введите длину стороны a: '))
    side_b = float(input('Введите длину стороны b: '))
    side_c = float(input('Введите длину стороны c: '))

    if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
        print('Треугольник с такими сторонами не существует')
    else:
        if side_a == side_b == side_c:
            print('Треугольник равносторонний')
        elif side_a == side_b or side_a == side_c or side_b == side_c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
except ValueError:
    print('Необходимо вводить целые или вещественные числа с точкой в качестве разделителя')
