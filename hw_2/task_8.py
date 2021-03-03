# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count_helper(value, digit, res=0):
    if value == 0:
        return res
    last = value % 10
    if digit == last:
        res += 1
    return count_helper(value // 10, digit, res)


def digit_counter(digit, _quantity, result=0):
    if _quantity == 0:
        return result
    new_user_value = int(input('Введите число -> '))
    result += count_helper(new_user_value, digit)
    return digit_counter(digit, _quantity - 1, result)


interest_digit = int(input('Введите интересующую цифру -> '))
quantity = int(input('Сколько чисел будет введено? -> '))

digit_quantity = digit_counter(interest_digit, quantity)
print(f'Ваша цифра {interest_digit} встречалась {digit_quantity}')