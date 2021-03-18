# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(left, right):
    output = [None] * (len(left) + len(right))

    # данный финт нужен чтобы упростисть логику слияния и уменьшить количество кода
    left.append(float('inf'))
    right.append(float('inf'))

    # индексы массивов левый и правый
    r_idx = l_idx = 0

    for i in range(len(left) + len(right) - 2):   # -2 нужно, чтобы не учитывать добавленные бесконечности
        if left[l_idx] < right[r_idx]:
            output[i] = left[l_idx]
            l_idx += 1
        else:
            output[i] = right[r_idx]
            r_idx += 1
    return output


def merge_sort(data):
    if len(data) < 2:
        return data

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def test_your_sort():
    # по условию задачи
    COUNT = 10
    BOTTOM = 0
    TOP = 49
    ARR_CNT = 10

    for _ in range(COUNT):
        arr = [random.random() * TOP + BOTTOM for _ in range(ARR_CNT)]

        sorted_check = sorted(arr)
        sorted_ = merge_sort(arr)
        assert sorted_ == sorted_check, f'{sorted_} failed {sorted_check}'
        print(arr)
        print(sorted_, '\n')
    print('Tests OK')


if __name__ == '__main__':

    test_your_sort()
