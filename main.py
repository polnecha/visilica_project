import random

# Список слов для игры
words = ['python', 'java', 'hangman', 'programming', 'development']

# Выбираем случайное слово из списка
word_to_guess = random.choice(words)

# Список для отображения угаданного слова с подставленными _ вместо букв
guessed_word = ['_'] * len(word_to_guess)

# Количество попыток (ошибок)
max_attempts = 6
attempts_left = max_attempts

# Множество для хранения уже введенных букв
guessed_letters = set()


hangman_images = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========''',  # 6 попыток (исходная ситуация)
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========''',  # 5 попыток
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========''',  # 4 попытки
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========''',  # 3 попытки
    '''
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========''',  # 2 попытки
    '''
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========''',  # 1 попытка
    '''
       -----
       |   |
       O   | 
      /|\\  |
      / \\  |
    ========='''  # 0 попыток, проигрыш
]


def display_game():
    print(hangman_images[max_attempts - attempts_left])  # Показываем картинку в зависимости от оставшихся попыток
    print('Текущее слово: ' + ' '.join(guessed_word))
    print(f'Оставшиеся попытки: {attempts_left}')
    print(f'Использованные буквы: {", ".join(sorted(guessed_letters))}')


def play_game():
    """
    Основная функция для проведения игры. Игрок вводит буквы, пытаясь угадать слово,
    получая штрафы за ошибки. Игра продолжается до тех пор, пока не будут угаданы все буквы
    или не закончится количество попыток.
    """
    global attempts_left

    # Игровой цикл, пока есть попытки
    while attempts_left > 0:
        # Отображаем текущее состояние игры
        display_game()

        # Получаем ввод от игрока
        guess = input('Введите букву: ').lower()

        # Проверка на корректность ввода
        if not guess.isalpha() or len(guess) != 1:
            print("Введите только одну букву.")
            continue

        # Проверка на повторный ввод буквы
        if guess in guessed_letters:
            print("Эта буква уже была введена.")
            continue

        # Добавляем букву в список использованных
        guessed_letters.add(guess)

        # Если буква есть в слове, обновляем состояние
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
            print("Угадали букву!")
        else:
            # Если буквы нет в слове, уменьшаем количество попыток
            attempts_left -= 1
            print(f"Ошибка! Буквы {guess} нет в слове.")

        # Проверка на победу (все буквы угаданы)
        if '_' not in guessed_word:
            display_game()  # Показываем финальное состояние при победе
            print('Поздравляем, вы угадали слово!')
            break
    else:
        # Если попытки закончились, выводим информацию о проигрыше
        display_game()  # Показываем финальное состояние при поражении
        print(f'Вы проиграли. Загаданное слово было: {word_to_guess}')

if __name__ == "__main__":
    play_game()
