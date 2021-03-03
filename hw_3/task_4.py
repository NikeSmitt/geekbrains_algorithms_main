# Определить, какое число в массиве встречается чаще всего.
import random


SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 5
src_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(src_array)

items_dict = {}
for item in src_array:
    count = items_dict.setdefault(item, 0)
    items_dict[item] = count + 1


max_freq_value = -1
max_freq_key = -1
for key, value in items_dict.items():
    if max_freq_value < value:
        max_freq_value = value
        max_freq_key = key
print(f'Max frequency {max_freq_value} has value {max_freq_key}')
