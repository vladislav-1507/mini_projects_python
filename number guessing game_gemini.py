from random import randint

print('Добро пожаловать в числовую угадайку')

ERROR_MESSAGE_NUMBER = "А может быть, все-таки введем целое число?"
ERROR_MESSAGE_RANGE = "А может быть, все-таки введем целое число от 1 до {}?"


def is_valid_number(num_str):
    """Проверяет, является ли строка целым числом."""
    return num_str.isdigit()

def is_in_range(num, min_val, max_val):
    """Проверяет, входит ли число в заданный диапазон."""
    return min_val <= num <= max_val


while True:
    print('Введите максимальное число, которое загадает система')
    max_number_str = input()

    while not is_valid_number(max_number_str):
        print(ERROR_MESSAGE_NUMBER)
        max_number_str = input()

    max_number = int(max_number_str)
    secret_number = randint(1, max_number)
    total_attempts = 0

    while True:
        user_input_str = input(f'Введите число от 1 до {max_number}: ')

        while not is_valid_number(user_input_str):
            print(ERROR_MESSAGE_RANGE.format(max_number))
            user_input_str = input(f'Введите число от 1 до {max_number}: ')

        user_number = int(user_input_str)

        if not is_in_range(user_number, 1, max_number):
             print(ERROR_MESSAGE_RANGE.format(max_number))
             continue

        total_attempts += 1

        if user_number < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > secret_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! Число попыток = {total_attempts}')
            print('Хотите сыграть еще? Да/Нет')
            user_answer = input().lower()
            if user_answer == 'да':
                break
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                exit()

