# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def analise(value, odd=0, even=0):
    if value == 0:
        return odd, even
    last = value % 10
    if last % 2:
        odd += 1
    else:
        even += 1
    return analise(value // 10, odd, even)


value = int(input('Введите натуральное число -> '))
value_odd, value_even = analise(value)
print(f'В числе {value}: {value_even} четных чисел(а) и {value_odd} нечетных')

