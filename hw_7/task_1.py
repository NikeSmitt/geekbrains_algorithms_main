# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Примечания: ● алгоритм сортировки
# должен быть в виде функции, которая принимает на вход массив данных, ● постарайтесь сделать алгоритм умнее,
# но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
# шейкерная и другие в зачёт не идут.
import random


def bubble_sort(data):
    data_copied = data.copy()
    if len(data_copied) < 2:
        return
    for i in range(len(data_copied) - 1, 0, -1):
        swapped = False
        for j in range(i):

            if data_copied[j] < data_copied[j + 1]:
                data_copied[j], data_copied[j + 1] = data_copied[j + 1], data_copied[j]
                swapped = True

        if not swapped:
            break

    return data_copied


def test_your_sort():
    # по условию задачи
    COUNT = 10
    BOTTOM = -100
    TOP = 99
    ARR_CNT = 10

    for _ in range(COUNT):
        array = [random.randint(BOTTOM, TOP) for _ in range(ARR_CNT)]

        sorted_check = sorted(array, reverse=True)

        b_sort = bubble_sort(array)

        assert b_sort == sorted_check, f'{b_sort} failed {sorted_check}'
        print(f'Origin array: {array}')
        print(f'Sorted array: {b_sort}', '\n')
    print('Tests OK')


if __name__ == "__main__":
    # array = [30, -81, -33, -46, 53, 69, -46, -94, -85, 13]
    # print(array)
    # print(bubble_sort(array))

    test_your_sort()
