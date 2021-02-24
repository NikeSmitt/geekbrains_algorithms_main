# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


#   a - 97
#   z - 122

letter_1 = input('Введите сточную букву -> ').strip()
letter_2 = input('Введите сточную букву -> ').strip()

let_1_pos = ord(letter_1) - 96

if letter_1 == letter_2:
    print(f'Позиция буквы {letter_1}: {let_1_pos}')
    print(f'Буквы одинаковые')

else:
    let_2_pos = ord(letter_2) - 96
    dist = abs(let_1_pos - let_2_pos) - 1

    print(f'Позиция буквы {letter_1}: {let_1_pos}')
    print(f'Позиция буквы {letter_2}: {let_2_pos}')
    print(f' Между {letter_1} и {letter_2}: {dist} букв(ы)')

