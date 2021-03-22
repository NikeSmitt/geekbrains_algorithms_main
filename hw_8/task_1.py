# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и
# строку целиком.
import hashlib


def task_1(text):
    if len(text) < 2:
        return 0
    text_length = len(text)
    word_length = 0
    words_hash = set()

    while word_length < text_length:
        position = 0
        word_length += 1
        while position + word_length <= text_length:
            word = text[position: word_length + position]
            words_hash.add(hashlib.sha1(word.encode()).hexdigest())
            position += 1
    return len(words_hash) - 1


print(task_1('abcb'))
print(task_1('papa'))
print(task_1('sova'))
print(task_1('a'))
print(task_1('python'))
