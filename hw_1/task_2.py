# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a, b = 5, 6
bit_and = a & b
bit_or = a | b
bit_xor = a ^ b
l_shift = a << 2
r_shift = a >> 2

print(f'{a} И {b} -> {bit_and}')
print(f'{a} ИЛИ {b} -> {bit_or}')
print(f'{a} ИСКЛ ИЛИ {b} -> {bit_xor}')
print(f'{a} сдвиг вдево на 2 -> {l_shift}, сдвиг вправо на 2 -> {r_shift}')
