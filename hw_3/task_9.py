# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


ROWS_COUNT = 3
COLUMNS_COUNT = 3
MIN_VALUE = 1
MAX_VALUE = 100

matrix = [[random.randint(MIN_VALUE, MAX_VALUE) for _ in range(COLUMNS_COUNT)] for _ in range(ROWS_COUNT)]

# list of min elem in columns
min_row = [0] * COLUMNS_COUNT

for col in range(COLUMNS_COUNT):
    # init with MAX value
    min_in_col = float('inf')

    # find min elem in column
    for row in range(ROWS_COUNT):
        if matrix[row][col] < min_in_col:
            min_in_col = matrix[row][col]

    # insert result in appropriate position
    min_row[col] = min_in_col

# find max in min_row
max_value = min_row[0]

for value in range(1, len(min_row)):
    if max_value < min_row[value]:
        max_value = min_row[value]

print(*matrix, sep='\n')
# print(min_row)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_value}')
