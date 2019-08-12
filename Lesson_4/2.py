"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""


def is_prime_number(n):
    for i in range(2, int(n ** 0.5 + 1.2)):
        if n % i == 0:
            return False
    return True


def get_prime_number_by_idx(idx):
    num = 5
    prime_numbers = [2, 3]
    while True:
        if is_prime_number(num):
            prime_numbers.append(num)
        if len(prime_numbers) == idx:
            return prime_numbers[-1]
        num += 2


idx = int(input('Введите индекс простого числа: '))

first_prime_nums = (2, 3)

print(idx, first_prime_nums[idx - 1]) if idx <= 2 else print(idx, get_prime_number_by_idx(idx))
