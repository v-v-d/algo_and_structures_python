"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


# Рекурсия
def guess_the_number_game(num, attempts, attempt=1):
    print(f'Попытка №{attempt}')
    try:
        user_answer = int(input('Угадайте число от 0 до 100: '))

        if user_answer == num:
            return 'Вы угадали!'
        if user_answer < num:
            print(f'Загаданное число больше {user_answer}')
        else:
            print(f'Загаданное число меньше {user_answer}')
    except ValueError:
        print('Ошибка! Необходимо ввести целое число от 0 до 100')
    if attempt < attempts:
        return guess_the_number_game(num, attempts, attempt + 1)
    else:
        return f'Вы проиграли. Было загадано число {num}'


random_number = random.randint(0, 100)
num_of_attempts = 10

# # Вывод рекурсии
# print(guess_the_number_game(random_number, num_of_attempts))

# Цикл
for attempt in range(num_of_attempts):
    print(f'Попытка №{attempt + 1}')
    try:
        user_answer = int(input('Угадайте число от 0 до 100: '))

        if user_answer == random_number:
            print('Вы угадали!')
            break
        if user_answer < random_number:
            print(f'Загаданное число больше {user_answer}')
        else:
            print(f'Загаданное число меньше {user_answer}')
    except ValueError:
        print('Ошибка! Необходимо ввести целое число от 0 до 100')

    if attempt == num_of_attempts - 1:
        print(f'Вы проиграли. Было загадано число {random_number}')
        break
