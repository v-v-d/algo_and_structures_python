#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letters = input('Введите две буквы в интервале a-z через пробел: ')

try:
    symbol_range = range(ord('a'), ord('z') + 1)
    letter1, letter2 = letters.split()

    if ord(letter1) in symbol_range and ord(letter2) in symbol_range:
        letter1_pos_in_alphabet = ord(letter1) - ord('a') + 1
        letter2_pos_in_alphabet = ord(letter2) - ord('a') + 1

        if letter2_pos_in_alphabet - letter1_pos_in_alphabet > 0:
            num_of_letters_between = abs(letter2_pos_in_alphabet - letter1_pos_in_alphabet) - 1
        else:
            num_of_letters_between = abs(letter2_pos_in_alphabet - letter1_pos_in_alphabet)

        print(f'Порядковый номер буквы {letter1} в алфавите: {letter1_pos_in_alphabet}')
        print(f'Порядковый номер буквы {letter2} в алфавите: {letter2_pos_in_alphabet}')
        print(f'Количество букв между {letter1} и {letter2}: {num_of_letters_between}')
    else:
        print('Необходимо ввести буквы в интервале a-z через пробел')

except ValueError:
    print('Необходимо ввести две буквы через пробел')
