# Определить, какое число в массиве встречается чаще всего.
# version 3

import random
import timeit
import cProfile


def get_array(size, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]


def task_1_3(arr):
    max_freq = -1
    max_freq_key = -1
    for key in arr:
        spam_freq = 0
        for candidate in arr:
            if candidate == key:
                spam_freq += 1
            for fake in arr:    # fake third loop
                a = fake + 1    #
        if max_freq < spam_freq:
            max_freq_key = key
            max_freq = spam_freq

    return max_freq_key, max_freq


# array = get_array(10)
# print(array)
# val, freq = task_1_3(array)
# print(f'Max frequency {freq} has value {val}')

print(timeit.timeit('task_1_3(get_array(100))', number=100, globals=globals()))  # 2.784980914
print(timeit.timeit('task_1_3(get_array(200))', number=100, globals=globals()))  # 21.358490755000002
print(timeit.timeit('task_1_3(get_array(400))', number=100, globals=globals()))  # 169.649446473


cProfile.run('task_1_3(get_array(1000))')

"""
         5265 function calls in 26.424 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   26.424   26.424 <string>:1(<module>)
     1000    0.001    0.000    0.001    0.000 random.py:238(_randbelow_with_getrandbits)
     1000    0.001    0.000    0.002    0.000 random.py:291(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:335(randint)
        1    0.000    0.000    0.002    0.002 task_1_3.py:10(<listcomp>)
        1   26.421   26.421   26.421   26.421 task_1_3.py:13(task_1_3)
        1    0.000    0.000    0.002    0.002 task_1_3.py:9(get_array)
        1    0.000    0.000   26.424   26.424 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1259    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

