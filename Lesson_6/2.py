"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
import random
from pympler import asizeof


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


hex_num_first = f'{random.randrange(16**10):10x}'.upper()
hex_num_second = f'{random.randrange(16**10):10x}'.upper()

obj_1 = HexOperation1(hex_num_first, hex_num_second)
print(obj_1.__dict__)
print(asizeof.asizeof(obj_1))

obj_2 = HexOperation2(hex_num_first, hex_num_second)
print(obj_2.__slots__)
print(asizeof.asizeof(obj_2))

# {'num_first': '2D8CB4B740', 'num_second': '78B3E92069'}
# 264
# ('num_first', 'num_second')
# 112

# Вывод:
# Использование __slots__ уменьшает кол-во потребляемой памяти экземпляром класса. В данном случае вместо словаря
# атрибуты храняться в кортеже.
