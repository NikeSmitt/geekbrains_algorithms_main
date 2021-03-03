# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1 + 2
# + ... + n = n(n + 1) / 2, где n — любое натуральное число.

import random

def task_7(n, summ=0):
    if n < 1:
        return summ
    new_summ = summ + n
    return task_7(n - 1, new_summ)


print("""Программа, проверяющая, что : 1 + 2 + ... + n = n(n + 1) / 2, где n E N""")
n = random.randint(1, 100)
res = task_7(n)
res_equation = n * (n + 1) // 2
if res == res_equation:
    print('Совпадают')
else:
    print('Не совпадают')
print(f'1 + 2 + ... + {n} = {res}\n{n} * ({n} + 1) / 2 = {res_equation}')
