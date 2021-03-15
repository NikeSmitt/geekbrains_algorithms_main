# Для каждого упражнения написать программную реализацию. Код пишите в файлах с расширением .py в кодировке UTF-8 (в
# PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать
# английские имена, например, les_6_task_1. Для оценки «Отлично» необходимо выполнить все требования, указанные в
# задании и примечаниях. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием
# памяти.

# platform: MacOS 11.2.2, x64 Intel Core i7, python 3.9
import random
from collections import deque
import sys


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


def add_two_hex_2(first, second):
    BASE = 16

    HEX_NUM = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
               6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
               12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    HEX_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

    consider_memory(BASE, memory_used)
    consider_memory(HEX_NUM, memory_used)
    consider_memory(HEX_INT, memory_used)

    def inner_sum(a, b, prev_carry):
        sum_ = HEX_INT[a] + HEX_INT[b] + prev_carry
        next_carry = sum_ // BASE
        idx = sum_ % BASE
        return f'{HEX_NUM[idx]}', next_carry

    first = deque(list(first))
    second = deque(list(second))

    # определяем какое число меньше и больше, чтобы при сложении в столбик "нижнее число было короче"
    lower, bigger = (first, second) if len(first) < len(second) else (second, first)

    consider_memory(first, memory_used)
    consider_memory(second, memory_used)

    consider_memory(lower, memory_used)
    consider_memory(bigger, memory_used)

    output = deque()
    carry = 0
    spam = 0

    while len(lower):
        spam, carry = inner_sum(lower.pop(), bigger.pop(), carry)
        output.appendleft(spam)

    while len(bigger):
        spam, carry = inner_sum('0', bigger.pop(), carry)
        output.appendleft(spam)

    if carry == 1:
        output.appendleft(str(carry))

    consider_memory(spam, memory_used)
    consider_memory(carry, memory_used)
    consider_memory(output, memory_used)

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

        checked_res = check_add(a, b)
        my_res = ''.join(add_two_hex_2(a, b))
        assert my_res == checked_res, f"Failed with {a} + {b} -> {my_res} != {checked_res}"

    print('Tests OK')


if __name__ == "__main__":
    # main()
    res = add_two_hex_2('1AB', '2AB')
    print(''.join(res))

    print(f'Суммарное потребление памяти для переменных -> {sum(memory_used):_} байт')
    # Суммарное потребление памяти для переменных -> 7_740 байт

    print(f'Колличество учтенных объектов: {len(memory_used)}')
    # Колличество учтенных объектов: 89
