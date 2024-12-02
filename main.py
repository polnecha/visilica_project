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