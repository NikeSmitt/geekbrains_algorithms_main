import timeit
import cProfile
import matplotlib.pyplot as plt


# Написать два алгоритма нахождения i-го по счету простого числа.


# Без использования решета Эрастофена

def is_prime(value):
    if value < 2:
        return False
    dev = 2
    while dev <= value ** 0.5:
        if value % dev == 0:
            return False
        dev += 1
    return True


def without_eratosfen(n):
    if n > 0:
        count = 0
        candidate = 1
        while count < n:
            candidate += 1
            if is_prime(candidate):
                count += 1

        return candidate


# С использованием решета Эратосфена
def with_eratosfen(n):

    INC = 100
    primes = [True] * INC
    primes[0] = primes[1] = False

    # основной счетчик простых чисел
    count = 0
    idx = 0
    last_prime = 0
    while count < n:
        add = 0

        # очередная стартовая позиция
        while not primes[idx]:
            idx += 1

        add = idx
        last_prime = idx
        count += 1

        # флаг для отслеживания необходимости расширять массив
        need_to_extend = True

        # исключаем все кратные idx
        while idx + add < len(primes):
            idx += add
            primes[idx] = False
            need_to_extend = False

        # если расширили, то просеивание необходимо повторять
        if need_to_extend:
            primes.extend([True] * INC)
            idx = 0
            count = 0
            continue

        idx = add + 1

    return last_prime


def test_tasks(func):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, value in enumerate(primes):
        assert func(i + 1) == value, f'{func.__name__} Test failed on {i + 1} number - {value}'
    else:
        print(f'{func.__name__}: Tests OK')


test_tasks(without_eratosfen)
test_tasks(with_eratosfen)




# print(timeit.timeit('without_eratosfen(10)', number=100, globals=globals())) # 0.0016512520000000058
# print(timeit.timeit('without_eratosfen(50)', number=100, globals=globals())) # 0.017440287
# print(timeit.timeit('without_eratosfen(250)', number=100, globals=globals())) # 0.17905873300000003
# print(timeit.timeit('without_eratosfen(1250)', number=100, globals=globals())) # 1.8562198520000002
#
# cProfile.run('without_eratosfen(1250)')

"""
         10180 function calls in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
    10176    0.017    0.000    0.017    0.000 task_2.py:10(is_prime)
        1    0.002    0.002    0.019    0.019 task_2.py:21(without_eratosfen)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# print(timeit.timeit('with_eratosfen(10)', number=100, globals=globals())) # 0.005089158000000003
# print(timeit.timeit('with_eratosfen(50)', number=100, globals=globals())) # 0.094234776
# print(timeit.timeit('with_eratosfen(250)', number=100, globals=globals())) # 0.79423713
# print(timeit.timeit('with_eratosfen(1250)', number=100, globals=globals())) # 7.648597774000001
#
# cProfile.run('with_eratosfen(1250)')

"""
         460088 function calls in 0.147 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.147    0.147 <string>:1(<module>)
        1    0.110    0.110    0.147    0.147 task_2.py:34(with_eratosfen)
        1    0.000    0.000    0.147    0.147 {built-in method builtins.exec}
   460068    0.036    0.000    0.036    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       16    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


"""


"""
C решетом результы значительно хуже, чем вариант без него. Все упирается в необходимость постоянно расширять 
основной массив и производить просеивание заного. Оба варианта можно оптимизировать. С решетом - можно применять сразу
большие массивы при значительном искомом номере простого числа. Определить эксперементально 
В варианте без решета - оптимизировать проверку на простое число (проверять только до sqrt(n))

График - https://drive.google.com/file/d/1LKMHnGT0OiRafVFPfXZAgD-3kMfATrl_/view?usp=sharing
"""

