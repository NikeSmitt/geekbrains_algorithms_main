# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


min_elem_idx = 0
max_elem_idx = 0
for idx in range(1, len(src_array)):
    if src_array[min_elem_idx] > src_array[idx]:
        min_elem_idx = idx
    elif src_array[max_elem_idx] < src_array[idx]:
        max_elem_idx = idx


print(src_array)
src_array[min_elem_idx], src_array[max_elem_idx] = src_array[max_elem_idx], src_array[min_elem_idx]
print(f'Indexes: min = {min_elem_idx} <-> max = {max_elem_idx}')
print(src_array)
