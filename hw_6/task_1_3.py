# Для каждого упражнения написать программную реализацию. Код пишите в файлах с расширением .py в кодировке UTF-8 (в
# PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать
# английские имена, например, les_6_task_1. Для оценки «Отлично» необходимо выполнить все требования, указанные в
# задании и примечаниях. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием
# памяти.

# platform: MacOS 11.2.2, x64 Intel Core i7, python 3.9

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


def add_two_hex_3(first, second):
    BASE = 16
    INT_NUM = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    HEX_NUM = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

    consider_memory(BASE, memory_used)
    consider_memory(HEX_NUM, memory_used)
    consider_memory(INT_NUM, memory_used)

    def inner_sum(a, b, prev_carry):
        sum_ = INT_NUM[HEX_NUM.index(a)] + INT_NUM[HEX_NUM.index(b)] + prev_carry
        next_carry = sum_ // BASE
        idx = sum_ % BASE
        return f'{HEX_NUM[idx]}', next_carry

    output = ''
    carry = 0
    spam = 0

    if len(first) > len(second):
        first, second = second, first

    second = f'{"0" * (len(first) - len(second))}{second}'

    consider_memory(first, memory_used)
    consider_memory(second, memory_used)

    while len(first):
        spam, carry = inner_sum(first[-1], second[-1], carry)
        output = f'{spam}{output}'
        first, second = first[:-1], second[:-1]

    if carry == 1:
        output = f'{carry}{output}'

    consider_memory(spam, memory_used)
    consider_memory(carry, memory_used)
    consider_memory(output, memory_used)

    return output


res = add_two_hex_3('1AB', '2AB')
print(res)
print(f'Суммарное потребление памяти для переменных -> {sum(memory_used):_} байт')
# Суммарное потребление памяти для переменных -> 1_838 байт
print(f'Колличество учтенных объектов: {len(memory_used)}')
# Колличество учтенных объектов: 40
