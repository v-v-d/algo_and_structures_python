"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""


class HexOperation1:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


class HexOperation2:
    __slots__ = ('num_first', 'num_second')

    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


hex_num_first = list(input('Введите первое шеснадцатиричное число: '))
hex_num_second = list(input('Введите второе шеснадцатиричное число: '))

res_sum = HexOperation1(hex_num_first, hex_num_second) + HexOperation1(hex_num_first, hex_num_second)
res_mul = HexOperation1(hex_num_first, hex_num_second) * HexOperation1(hex_num_first, hex_num_second)
print(f'Сумма чисел = {res_sum}\nПроизведение чисел = {res_mul}')
