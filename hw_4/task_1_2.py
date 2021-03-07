# Определить, какое число в массиве встречается чаще всего.
# version 2
import random
import timeit
import cProfile


def get_array(size, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(size)]


def task_1_2(arr):
    max_freq = -1
    max_freq_key = -1
    for key in arr:
        spam_freq = 0
        for candidate in arr:
            if candidate == key:
                spam_freq += 1
        if max_freq < spam_freq:
            max_freq_key = key
            max_freq = spam_freq

    return max_freq_key, max_freq


# array = get_array(10)
# print(array)
# val, freq = task_1_2(array)
# print(f'Max frequency {freq} has value {val}')

# print(timeit.timeit('task_1_2(get_array(100))', number=100, globals=globals()))  # 0.039003
# print(timeit.timeit('task_1_2(get_array(500))', number=100, globals=globals()))  # 0.6785252869999999
# print(timeit.timeit('task_1_2(get_array(1000))', number=100, globals=globals()))  # 2.538098217
# print(timeit.timeit('task_1_2(get_array(2000))', number=100, globals=globals()))  # 9.993290442
# print(timeit.timeit('task_1_2(get_array(4000))', number=100, globals=globals()))  # 40.422748639
#
#
# cProfile.run('task_1_2(get_array(4000))')


"""
          21179 function calls in 0.399 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.399    0.399 <string>:1(<module>)
     4000    0.002    0.000    0.002    0.000 random.py:238(_randbelow_with_getrandbits)
     4000    0.002    0.000    0.005    0.000 random.py:291(randrange)
     4000    0.001    0.000    0.006    0.000 random.py:335(randint)
        1    0.392    0.392    0.392    0.392 task_1_2.py:12(task_1_2)
        1    0.000    0.000    0.007    0.007 task_1_2.py:8(get_array)
        1    0.001    0.001    0.007    0.007 task_1_2.py:9(<listcomp>)
        1    0.000    0.000    0.399    0.399 {built-in method builtins.exec}
     4000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5173    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""


x1 = []
y1 = []

for n in range(10, 1000, 50):
    y1.append(timeit.timeit(f'task_1_2(get_array({n}))', number=100, globals=globals()))
    x1.append(n)

print(y1)
print(x1)