# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def get_median(data):
    data_ = data.copy()
    key = 0

    for i in range(len(data_)):
        # счетчики для элементов больше, меньше, равные
        left_count = 0
        right_count = 0
        eq_count = 0

        # очередной элемент ставим в начало, чтобы упростить пробег по всем остальным, потом вернем его на место
        data_[key], data_[i] = data_[i], data_[key]

        # бежим со второго элемента и скравниваем с первым
        for j in range(1, len(data_)):
            if data_[key] > data_[j]:
                left_count += 1
            elif data_[key] < data_[j]:
                right_count += 1
            else:
                eq_count += 1

        if left_count == right_count or eq_count == abs(left_count - right_count) or eq_count >= len(data_) // 2:
            return data_[key]

        # возвращаем элемент на место
        data_[key], data_[i] = data_[i], data_[key]


def test_median():
    COUNT = 11
    BOTTOM = 0
    TOP = 49
    ARR_CNT = 11  # использовать только! не четное число

    for _ in range(COUNT):
        array = [random.randint(BOTTOM, TOP) for _ in range(ARR_CNT)]

        median_check = sorted(array)[len(array) // 2]
        median = get_median(array)
        assert median == median_check, f' Failed {median_check} in {array}, your: {median}'

    print('Tests OK')


if __name__ == "__main__":
    arr = [5, 1, 2, 6, 3]
    print(f'Медиана в {arr}: {get_median(arr)}')

    arr = [0, 0, 0, 1, 1]
    print(f'Медиана в {arr}: {get_median(arr)}')

    arr = [1, 1, 2]
    print(f'Медиана в {arr}: {get_median(arr)}')

    test_median()
