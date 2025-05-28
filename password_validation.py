'''Хороший пароль по условиям этой задачи состоит как минимум из 
7 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.'''
def password_validation(pswrd):
    if len(pswrd) >= 7:
        return all([any(map(lambda el: el.isdigit(), pswrd)), any(map(lambda el: el.isupper(), pswrd)), any(map(lambda el: el.islower(), pswrd))])
    else:
        return False

print('YES' if password_validation(input()) else 'NO')