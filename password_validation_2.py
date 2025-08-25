from string import ascii_lowercase, ascii_uppercase, digits

def verification(login, password, success, failure):
    '''проверяет пароль на наличие заглавных, строчных
    символов и цифр'''
    upper_flag, lower_flag, digit_flag = False, False, False
    message1 = 'в пароле нет ни одной буквы'
    message2 = 'в пароле нет ни одной заглавной буквы'
    message3 = 'в пароле нет ни одной строчной буквы'
    message4 = 'в пароле нет ни одной цифры'

    for w in password:
        if w in ascii_uppercase:
            upper_flag = True
        if w in ascii_lowercase:
            lower_flag = True
        if w in digits:
            digit_flag = True
            
    if all((upper_flag, lower_flag, digit_flag)):
        success(login)
    elif not upper_flag and not lower_flag:
        failure(login, message1)
    elif not upper_flag and lower_flag:
        failure(login, message2)
    elif upper_flag and not lower_flag:
        failure(login, message3)
    elif not digit_flag:
        failure(login, message4)
        
def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)

print(verification.__name__, verification.__doc__, verification.__defaults__, sep='\n')