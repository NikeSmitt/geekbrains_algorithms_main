# Определить, какое число в массиве встречается чаще всего.
# version 1
import random
import timeit
import cProfile


def get_array(size, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]

def task_1_1(arr):
    items_dict = {}
    for item in arr:
        count = items_dict.setdefault(item, 0)
        items_dict[item] = count + 1

    max_freq = -1
    max_freq_key = -1
    for key, value in items_dict.items():
        if max_freq < value:
            max_freq = value
            max_freq_key = key
    return max_freq_key, max_freq


# val, freq = task_1_1(get_array(100))
# print(f'Max frequency {freq} has value {val}')

print(timeit.timeit('task_1_1(get_array(100))', number=100, globals=globals()))  # 0.012792393999999999
print(timeit.timeit('task_1_1(get_array(500))', number=100, globals=globals()))  # 0.052088553
print(timeit.timeit('task_1_1(get_array(1000))', number=100, globals=globals()))  # 0.09439028599999999
print(timeit.timeit('task_1_1(get_array(2000))', number=100, globals=globals()))  # 0.188407993
print(timeit.timeit('task_1_1(get_array(4000))', number=100, globals=globals()))  # 0.36551380699999997


cProfile.run('task_1_1(get_array(4000))')


"""
         25108 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
     4000    0.002    0.000    0.002    0.000 random.py:238(_randbelow_with_getrandbits)
     4000    0.002    0.000    0.004    0.000 random.py:291(randrange)
     4000    0.001    0.000    0.006    0.000 random.py:335(randint)
        1    0.001    0.001    0.001    0.001 task_1_1.py:10(task_1_1)
        1    0.000    0.000    0.006    0.006 task_1_1.py:7(get_array)
        1    0.001    0.001    0.006    0.006 task_1_1.py:8(<listcomp>)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5101    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
     4000    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}


"""

