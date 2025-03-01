from random import choice

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

count_of_passwords = int(input('Сколько паролей нужно сгенерировать? '))
length_of_password = int(input('Какая должна быть длина пароля? '))
answer1 = input('Включать ли прописные буквы? (Да/Нет) ')
if answer1.lower() == 'да':
    chars += uppercase_letters
answer2 = input('Включать ли строчные буквы? (Да/Нет) ')
if answer2.lower() == 'да':
    chars += lowercase_letters
answer3 = input('Включать ли цифры? (Да/Нет) ')
if answer3.lower() == 'да':
    chars += digits
answer4 = input('Включать ли символы? (Да/Нет) ')
if answer4.lower() == 'да':
    chars += punctuation
answer5 = input('Исключать ли неоднозначные символы il1Lo0O? (Да/Нет) ')
if answer5.lower() == 'да':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('O', '')

for i in range(count_of_passwords):
    print(generate_password(length_of_password, chars))