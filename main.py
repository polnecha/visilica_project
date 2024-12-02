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

def display_game():
    print(hangman_images[max_attempts - attempts_left])  # Показываем картинку в зависимости от оставшихся попыток
    print('Текущее слово: ' + ' '.join(guessed_word))
    print(f'Оставшиеся попытки: {attempts_left}')
    print(f'Использованные буквы: {", ".join(sorted(guessed_letters))}')
