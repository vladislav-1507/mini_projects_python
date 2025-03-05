from random import choice

word_list = ['день', 'неделя', 'месяц', 'год']

# функция, возвращающая случайное слово
def get_word():
    return choice(word_list).upper()


'''значение tries = 6 соответствует начальному положению, пустая виселица;
значение tries = 0 соответствует конечному положению, то есть проигрышу 
и полностью нарисованному телу повешенного. '''

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input('Введите букву или слово: ').upper() 
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже назвали букву', guess)
            elif guess not in word:
                print(guess, 'не найдена в загаданном слове')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Вы угадали букву', guess)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже назвали слово', guess)
            elif guess != word:
                print(guess, 'не найдено в загаданном слове')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Некорректный ввод')
        print(display_hangman(tries))
        print(word_completion)
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы проиграли! Загаданное слово было: ', word) 
        
def main():
    while True:
        word = get_word()
        play(word)
        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            break

if __name__ == "__main__":
    main()