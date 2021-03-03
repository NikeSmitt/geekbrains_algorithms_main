# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив 
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.
import random


SIZE = 15
MIN_ITEM = 1
MAX_ITEM = 100
src_arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

output_arr = []
for idx, item in enumerate(src_arr):
    if item % 2 == 0:
        output_arr.append(idx)

print(src_arr)
print(output_arr)
