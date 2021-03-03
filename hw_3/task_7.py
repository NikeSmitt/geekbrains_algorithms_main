# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
import random


SIZE = 5
MIN_ITEM = -10
MAX_ITEM = 10
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(src_array)

# there are positions of two min elements
min_1_idx = 0
min_2_idx = 1


for idx in range(2, len(src_array)):
    if src_array[idx] < src_array[min_1_idx]:
        min_1_idx = idx
    if src_array[min_1_idx] < src_array[min_2_idx]:
        min_1_idx, min_2_idx = min_2_idx, min_1_idx

print(f'First min element: {src_array[min_1_idx]}')
print(f'Second min element: {src_array[min_2_idx]}')

