# Задание №1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
#  алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#  постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100 - 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

random.shuffle(array)
print(f'Исходный массив:\n\t{array}')
print('=' * 100)
print(f'Максимальное значение= {max(array)}, Минимальное значение = {min(array)}')
print('=' * 100)

'''
def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
'''


def bubble_sort(array, sort):
    # Функция сортировка методом "пузырька":
    # :param array: - массив
    # :param sort: - значение "up" - сортирует по возрастанию, "down" - по убыванию
    # :return: - отсортированный массив

    if sort == "up":
        n = 1
        while n < len(array):
            for i in range(len(array) - n):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            n += 1
        return array

    if sort == "down":
        n = 1
        while n < len(array):
            for i in range(len(array) - n):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            n += 1
        return array


print(f'Отсортированный по убыванию массив:\n\t{bubble_sort(array, "up")}')
print('=' * 100)
