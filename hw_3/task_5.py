# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 50
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_negative_idx = -1
max_negative_value = float('-inf')
for i, value in enumerate(src_array):
    if 0 > value > max_negative_value:
        max_negative_idx = i
        max_negative_value = value

print(src_array)
if max_negative_idx > -1:
    print(f'Максимальный отрицательный элемент: {src_array[max_negative_idx]} в позиции {max_negative_idx}')
else:
    print('Максимальный отрицательный элемент отсутствует')

