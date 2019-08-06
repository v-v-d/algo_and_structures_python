# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

lst = [i for i in range(2, 100)]

for i in range(2, 10):
    nums_qty = len([num for num in lst if num % i == 0])
    print(f'В диапазоне от 2 до 99 {nums_qty} чисел кратны {i}')
