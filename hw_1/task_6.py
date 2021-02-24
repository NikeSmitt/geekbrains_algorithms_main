# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

position = int(input('Введите номер строчной буквы в английском алфавите -> ').strip())
if 0 < position < 27:
    letter = chr(position + 96)
    print(f'На позиции {position} буква {letter}')
else:
    print('Ошшибка ввода')