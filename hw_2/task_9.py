# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.

def sum_helper(number, sum_res=0):
    if number == 0:
        return sum_res
    last = number % 10
    sum_res += last
    return sum_helper(number // 10, sum_res)


def max_digit_sum(max_sum=0, value_max_sum=0):
    value = int(input('Введите число (0 для выхода) -> '))
    if value == 0:
        return value_max_sum, max_sum
    new_sum = sum_helper(value)
    if max_sum < new_sum:
        max_sum = new_sum
        value_max_sum = value
    return max_digit_sum(max_sum, value_max_sum)


m_value, summary = max_digit_sum()
print(f'Макс сумма: {summary} у числа {m_value}')

