from random import choice, shuffle

# Константы
BALL_ANSWERS_RU = [
    "Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
    "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
    "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
    "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"
]

BALL_ANSWERS_EN = [
    "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
    "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
    "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
    "Very doubtful"
]

def get_user_name():
    """Получает имя пользователя."""
    name = input('Как тебя зовут? ')
    print('Привет,', name)
    return name

def get_language():
    """Спрашивает у пользователя предпочитаемый язык"""
    while True:
        lang = input("Выберите язык (русский/английский): ").lower()
        if lang in ("русский", "английский"):
            return lang
        else:
            print("Некорректный ввод. Пожалуйста, введите 'русский' или 'английский'.")

def get_answer(name, answers):
    """Возвращает случайный ответ, возможно, с именем пользователя."""
    answer = choice(answers)
    if ' ' in answer and choice([True, False]): #Добавляем имя пользователя в ответ с вероятностью 50%
        answer = f'{name}, {answer}'
    return answer

def ask_question(name, answers):
    """Задает вопрос пользователю и выводит ответ."""
    question = input('Задай свой вопрос: ')
    print(get_answer(name, answers))

def play_again():
    """Спрашивает, хочет ли пользователь задать еще вопрос."""
    while True:
        user_answer = input('Хотите задать еще вопрос? Да/Нет ').lower()
        if user_answer in ("да", "нет"):
            return user_answer == "да"
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")
def goodbye():
    """Прощание с пользователем."""
    print('Спасибо, что обратились к магическому шару! Возвращайся, если возникнут вопросы!')

def main():
    """Основная функция игры."""
    print('Привет, я магический шар, и я знаю ответ на любой твой вопрос')

    name = get_user_name()
    language = get_language()
    
    if language == "русский":
        answers = BALL_ANSWERS_RU[:]
    else:
        answers = BALL_ANSWERS_EN[:]

    shuffle(answers)

    while True:
        ask_question(name, answers)
        if not play_again():
            goodbye()
            break

if __name__ == "__main__":
    main()
