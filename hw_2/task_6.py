# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.

import random

def task_6(secret, value, attempts):
    if value == secret:
        print('Вы выйграли')
        return

    if attempts < 1:
        print('Вы проиграли')
        return

    prompt = 'Число больше' if value < secret else 'Число меньше'
    print(prompt)

    next_user_input = int(input('Угадайте число от 1 до 100 -> '))
    return task_6(secret, next_user_input, attempts - 1)


attempts = 10
secret = random.randint(1, 100)
user_input = int(input('Угадайте число от 1 до 100 -> '))
task_6(secret, user_input, attempts)
