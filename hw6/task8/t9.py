from itertools import product


def my_t9(digits):
    # Словарь, соответствующий цифрам клавиатуры
    digit_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    # Загрузка списка слов английского языка
    with open('words.txt', 'r') as file:
        english_words = set(word.strip().lower() for word in file)

    # Генерация всех возможных комбинаций букв из цифр
    possible_combinations = [''.join(letters) for letters in product(*(digit_letters[d] for d in digits))]

    # Фильтрация комбинаций и оставление только тех, которые являются словами английского языка
    valid_words = [word for word in possible_combinations if word in english_words]

    return valid_words


# Пример использования
result = my_t9('22736368')
print(result)  # ['basement', 'casement']
