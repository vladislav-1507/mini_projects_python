import functools

def get_biggest(numbers):
    if len(numbers) == 0:
        res = -1
    else:
        # 1. Преобразуем все числа в строки
        str_numbers = [str(n) for n in numbers]

        # 2. Определяем функцию сравнения для сортировки
        # s1 идет перед s2, если s1+s2 > s2+s1
        def compare_numbers(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1  # s1 "меньше" (идет раньше) в контексте нашей сортировки
            elif s1 + s2 < s2 + s1:
                return 1   # s1 "больше" (идет позже)
            return 0

        # 3. Сортируем строки с использованием нашего компаратора
        # functools.cmp_to_key адаптирует нашу двух-аргументную compare_numbers
        # для использования в качестве key-функции в sorted(), которая ожидает одно-аргументную функцию.
        sorted_str_numbers = sorted(str_numbers, key=functools.cmp_to_key(compare_numbers))

        # 4. Объединяем отсортированные строки и преобразуем в число
        largest_number_str = "".join(sorted_str_numbers)

        # Обработка случая, если все числа были нули, например [0, 0] -> "00" -> 0
        if largest_number_str.startswith('0') and len(largest_number_str) > 1 and all(c == '0' for c in largest_number_str) :
            res = 0
        else:
            res = int(largest_number_str)

    return resimport functools

def get_biggest(numbers):
    if len(numbers) == 0:
        res = -1
    else:
        # 1. Преобразуем все числа в строки
        str_numbers = [str(n) for n in numbers]

        # 2. Определяем функцию сравнения для сортировки
        # s1 идет перед s2, если s1+s2 > s2+s1
        def compare_numbers(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1  # s1 "меньше" (идет раньше) в контексте нашей сортировки
            elif s1 + s2 < s2 + s1:
                return 1   # s1 "больше" (идет позже)
            return 0

        # 3. Сортируем строки с использованием нашего компаратора
        sorted_str_numbers = sorted(str_numbers, key=functools.cmp_to_key(compare_numbers))

        # 4. Объединяем отсортированные строки и преобразуем в число
        largest_number_str = "".join(sorted_str_numbers)

        # Обработка случая, если все числа были нули, например [0, 0] -> "00" -> 0
        if largest_number_str.startswith('0') and len(largest_number_str) > 1 and all(c == '0' for c in largest_number_str) :
            res = 0
        else:
            res = int(largest_number_str)

    return res