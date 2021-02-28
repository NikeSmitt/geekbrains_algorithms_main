# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

def task_3(value, rev_value=0):
    if value == 0:
        return rev_value
    last = value % 10
    rev_value = rev_value * 10 + last

    return task_3(value // 10, rev_value)


user_value = int(input('Введите натуральное число -> '))
reversed_value = task_3(user_value)
print(f'{user_value} -> {reversed_value}')