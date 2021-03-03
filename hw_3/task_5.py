# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 50
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_negative_idx = 0
for i in range(1, len(src_array)):
    if 0 > src_array[i] > src_array[max_negative_idx]:
        max_negative_idx = i

print(src_array)
print(f'Максимальный отрицательный элемент: {src_array[max_negative_idx]}')
