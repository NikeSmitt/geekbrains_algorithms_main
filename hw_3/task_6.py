# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.
import random


SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# find min, max elements
min_idx = 0
max_idx = 0

for idx, value in enumerate(src_array):
    if src_array[min_idx] > value:
        min_idx = idx
    if src_array[max_idx] < value:
        max_idx = idx

# for range
start, stop = (min_idx, max_idx) if min_idx <= max_idx else (max_idx, min_idx)

# sum all elements between them
sum_ = 0
for i in range(start + 1, stop):
    sum_ += src_array[i]


print(src_array)
print(f'Min элемент в позиции {min_idx} = {src_array[min_idx]}')
print(f'Max элемент в позиции {max_idx} = {src_array[max_idx]}')
print(f'Сумма элементов между ними: {sum_}')

