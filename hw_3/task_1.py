# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.

# START = 2
STOP = 100
MIN_NUMBER = 2
MAX_NUMBER = 10

output = [None] * MAX_NUMBER
for i in range(MIN_NUMBER, MAX_NUMBER):
    runner = i
    output[i] = 0

    while runner < STOP:
        output[i] += 1
        runner += i

# print table
for row in range(MIN_NUMBER, MAX_NUMBER):
    print(f'{row} -> {output[row]}')
