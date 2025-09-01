import functools


# Декоратор, который будет считать вызовы функции
def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # СТРОКА wrapper.num += 1: Выполняется при КАЖДОМ вызове декорированной функции.
        # Увеличивает атрибут 'num', который "прикреплен" к самой функции wrapper.
        wrapper.num += 1
        print(f"Вызов {func.__name__}: {wrapper.num}")
        val = func(*args, **kwargs)
        return val

    # СТРОКА wrapper.num = 0: Выполняется ОДИН РАЗ, когда декоратор применяется к функции.
    # Создает и инициализирует атрибут 'num' на объекте функции wrapper.
    wrapper.num = 0
    return wrapper


@counter
def greet(name):
    return f"Hello {name}!"


print(greet("Timur"))
print(greet("Ruslan"))
print(greet("Arthur"))
print(greet("Gvido"))
