"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’,
‘C’, ‘9’, ‘F’, ‘E’]. """

from collections import defaultdict
from collections import deque
import random

# создаем словари для преобразования hex <-> int
hex_int = defaultdict(int)
int_hex = defaultdict(str)
hex_row = '0123456789ABCDEF'

for i, value in enumerate(hex_row):
    hex_int[value] = i
    int_hex[i] = value


def add_two_hex(v1, v2, hex_to_int, int_to_hex):
    # чтобы не дублировать код, складывает две цифры (фрагмент сложения в столбик)
    def inner_sum(a, b, prev_carry):
        sum_ = hex_to_int[a] + hex_to_int[b] + prev_carry
        next_carry = sum_ // 16
        idx = sum_ % 16
        return f'{int_to_hex[idx]}', next_carry

    # вывод
    output = ''

    # следующий порядок
    carry = 0

    # переводим в list прописными буквами
    v1_l = list(v1.upper())
    v2_l = list(v2.upper())

    # определяем какое число меньше и больше, чтобы при сложении в столбик "нижнее число было короче"
    lower, bigger = (v1_l, v2_l) if len(v1_l) < len(v2_l) else (v2_l, v1_l)

    while len(lower):
        spam, carry = inner_sum(lower.pop(), bigger.pop(), carry)
        output = f'{spam}{output}'

    while len(bigger):
        spam, carry = inner_sum('0', bigger.pop(), carry)
        output = f'{spam}{output}'

    if carry:
        output = f'{carry}{output}'

    return output


def mult_hex(v1, v2, hex_to_int, int_to_hex):
    # проверка умножения на ноль
    if v1 == '0' or v2 == '0':
        return '0'

    # умножение одной цифры на другую с добавлением предыдущего десятка
    def inner_mult(a, b, prev_carry):
        sum_ = hex_to_int[a] * hex_to_int[b] + prev_carry
        next_carry, idx = divmod(sum_, 16)
        return f'{int_to_hex[idx]}', next_carry

    # используется для сохранения промежуточных результатов умножения
    queue = deque([])

    v1_l = list(v1.upper())
    v2_l = list(v2.upper())

    # ищим меньшее и большее, только для того чтобы меньшее число было 'снизу' в столбике
    lower, bigger = (v1_l, v2_l) if len(v1_l) < len(v2_l) else (v2_l, v1_l)

    for idx_lower, digit_lower in enumerate(lower[::-1]):
        carry = 0
        temp_value = ''
        for digit_bigger in bigger[::-1]:
            spam, carry = inner_mult(digit_bigger, digit_lower, carry)
            temp_value = f'{spam}{temp_value}'
        if carry:
            temp_value = f'{int_to_hex[carry]}{temp_value}'
        queue.append(f'{temp_value}{"0" * idx_lower}')

    # складываем промежуточные результаты умножения, используя уже имеющую функцию
    output = queue.popleft()
    while queue:
        output = add_two_hex(output, queue.popleft(), hex_to_int, int_to_hex)

    return output


# вспомогательные функции для проверки

def check_add(v1, v2):
    v1_int = int(f'0x{v1}', base=16)
    v2_int = int(f'0x{v2}', base=16)
    return hex(v1_int + v2_int)[2:].upper()


def check_mult(v1, v2):
    v1_int = int(f'0x{v1}', base=16)
    v2_int = int(f'0x{v2}', base=16)
    return hex(v1_int * v2_int)[2:].upper()


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

        checked_res, my_res = check_mult(a, b), mult_hex(a, b, hex_to_int=hex_int, int_to_hex=int_hex)
        assert my_res == checked_res, f"Failed with {a} * {b} -> {my_res} != {checked_res}"
    print('Tests OK')


if __name__ == "__main__":
    main()
