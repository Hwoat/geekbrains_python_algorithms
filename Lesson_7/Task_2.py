# Задание №2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


random.shuffle(array)
print(f'Исходный массив:\n\t{array}')
print('=' * 100)
print(f'Максимальное значение= {max(array)}, Минимальное значение = {min(array)}')
print('=' * 100)


def sort_merge(array):
    # Функция сортировка методом слияния:
    # param array - массив
    # return - отсортированный массив

    if len(array) <= 1:
        return array[:]
    else:
        mid = len(array) // 2
        left_array = sort_merge(array[:mid])
        right_array = sort_merge(array[mid:])

        return merge(left_array, right_array)


def merge(left, right):

    # Промежуточная функция слияния двух отсортированных массивов:
    # :param left: левый массив
    # :param right: правый массив
    # :return: отсортированный слитые в единый массив

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print(f'Отсортированный массив\n\t'{sort_merge(array)}')