num = int(input('введите число '))
new_osn = int(input('введите новую систему '))


def system_exchange(num, new_osn):
    """Переводит число из десятичной системы счисления в систему с основанием new_osn."""

    if new_osn < 2 or new_osn > 36:
        return "Основание системы счисления должно быть от 2 до 36."
    
    if num == 0:
      return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Символы для представления цифр
    result = ""

    while num > 0:
        digit = num % new_osn
        result = digits[digit] + result  # Добавляем цифру в начало строки
        num //= new_osn

    return result


print(system_exchange(num, new_osn))