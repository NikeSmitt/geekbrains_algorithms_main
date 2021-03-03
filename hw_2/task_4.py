# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.

def tast_4(remain, current_value=1.0, sum_result=1.0):
    if remain == 1:
        return sum_result
    COEF = -0.5
    next_value = current_value * COEF
    return tast_4(remain - 1, next_value, sum_result + next_value)


n = int(input('Введите номер элемента (натуральное число) -> '))
if n <= 0:
    res = 0
else:
    res = tast_4(n)
print(f'Сумма = {res}')
