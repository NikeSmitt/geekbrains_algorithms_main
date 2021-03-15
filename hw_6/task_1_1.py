# Для каждого упражнения написать программную реализацию. Код пишите в файлах с расширением .py в кодировке UTF-8 (в
# PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать
# английские имена, например, les_6_task_1. Для оценки «Отлично» необходимо выполнить все требования, указанные в
# задании и примечаниях. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием
# памяти.

# platform: MacOS 11.2.2, x64 Intel Core i7, python 3.9

import sys
from collections import defaultdict
import random


def consider_memory(obj, memory_used_list):
    _size = sys.getsizeof(obj)
    # print(f'{obj=},' f'{type(obj)=},', f'{_size=}')
    memory_used_list.append(_size)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for k, v in obj.items():
                consider_memory(k, memory_used_list)
                consider_memory(v, memory_used_list)
        elif not isinstance(obj, str):
            for item in obj:
                consider_memory(item, memory_used_list)


# лист, в котором будут храниться значения использования памяти
memory_used = []

# создаем словари для преобразования hex <-> int
hex_int = defaultdict(int)
int_hex = defaultdict(str)
hex_row = '0123456789ABCDEF'

for i, value in enumerate(hex_row):
    hex_int[value] = i
    int_hex[i] = value

consider_memory(i, memory_used)
consider_memory(value, memory_used)
consider_memory(hex_int, memory_used)
consider_memory(int_hex, memory_used)
consider_memory(hex_row, memory_used)


def add_two_hex(v1, v2, hex_to_int, int_to_hex):
    # чтобы не дублировать код, складывает две цифры (фрагмент сложения в столбик)
    def inner_sum(a, b, prev_carry):
        sum_ = hex_to_int[a] + hex_to_int[b] + prev_carry
        next_carry = sum_ // 16
        idx = sum_ % 16
        return f'{int_to_hex[idx]}', next_carry

    # магическое число тоже стоит учесть()
    consider_memory(16, memory_used)
    # вывод
    output = ''

    # следующий порядок
    carry = 0

    # переводим в list прописными буквами
    v1_l = list(v1.upper())
    v2_l = list(v2.upper())

    consider_memory(v1_l, memory_used)
    consider_memory(v2_l, memory_used)

    # определяем какое число меньше и больше, чтобы при сложении в столбик "нижнее число было короче"
    lower, bigger = (v1_l, v2_l) if len(v1_l) < len(v2_l) else (v2_l, v1_l)
    # создал дополнительно, чтобы учесть данную переменную, если в циклы не войдем
    spam = ''

    consider_memory(lower, memory_used)
    consider_memory(bigger, memory_used)

    while len(lower):
        spam, carry = inner_sum(lower.pop(), bigger.pop(), carry)
        output = f'{spam}{output}'

    while len(bigger):
        spam, carry = inner_sum('0', bigger.pop(), carry)
        output = f'{spam}{output}'

    if carry:
        output = f'{carry}{output}'

    consider_memory(output, memory_used)
    consider_memory(carry, memory_used)
    consider_memory(spam, memory_used)

    return output





def check_add(v1, v2):
    v1_int = int(f'0x{v1}', base=16)
    v2_int = int(f'0x{v2}', base=16)
    return hex(v1_int + v2_int)[2:].upper()


def main():

    # проверка
    LOWER = 10
    UPPER = 1000
    COUNT = 100
    for _ in range(COUNT):
        a = hex(random.randint(LOWER, UPPER))[2:].upper()
        b = hex(random.randint(LOWER, UPPER))[2:].upper()

        checked_res, my_res = check_add(a, b), add_two_hex(a, b, hex_to_int=hex_int, int_to_hex=int_hex)
        assert my_res == checked_res, f"Failed with {a} + {b} -> {my_res} != {checked_res}"

    print('Tests OK')


if __name__ == "__main__":
    # main()
    res = add_two_hex('1AB', '2AB', hex_int, int_hex)
    print(res)
    print(f'Суммарное потребление памяти для переменных -> {sum(memory_used):_} байт')
    # Суммарное потребление памяти для переменных -> 5_001 байт
    print(f'Колличество учтенных объектов: {len(memory_used)}')
    # Колличество учтенных объектов: 89