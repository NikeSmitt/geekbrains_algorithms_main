# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

ROWS_COUNT = 5
COLUMNS_COUNT = 4

matrix = []
for i in range(ROWS_COUNT):
    # row with user input
    row = list(map(int, input(f'Введите {COLUMNS_COUNT - 1} числа {i + 1} строки матрицы через пробел: ').split()))

    sum_ = 0
    for value in row:
        sum_ += value

    row.append(sum_)
    matrix.append(row)

print(*matrix, sep='\n')
