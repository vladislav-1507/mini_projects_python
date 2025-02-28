from random import randint

print('Добро пожаловать в числовую угадайку')


def is_valid_user_input(num):
    if num.isdigit():
        num = int(num)
        if num in range(1, n + 1):
            return True
        else:
            return False
    else:
        return False


def is_valid_range(num):
    if num.isdigit():
        return True
    else:
        return False


while True:

    print('Введите максимальное число, которое загадает система')
    n = input()
    if is_valid_range(n):
        n = int(n)
    else:
        print('А может быть все-таки введем целое число?')
        continue

    secret_number = randint(1, n)
    total_attempts = 0

    while True:
        user_input = input(f'Введите число от 1 до {n}: ')
        if is_valid_user_input(user_input):
            user_number = int(user_input)
            total_attempts += 1
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue

        if user_number < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > secret_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! Число попыток = {total_attempts}')
            print('Хотите сыграть еще? Да/Нет')
            user_answer = input()
            if user_answer.lower() == 'да':
                break
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                exit()
