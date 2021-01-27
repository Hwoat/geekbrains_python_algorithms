# Задание 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random as rnd

size = int(input("Введите количество элементов массива: "))
array = [rnd.randint(0, 100) for _ in range(size)]

array_min = 0
array_max = 0


print(f'Исходный массив: {array};')

for i in range(1, len(array)):
    if array[i] < array[array_min]:
        array_min = i
    elif array[i] > array[array_max]:
        array_max = i

print(f'Минимальное число: {array[array_min]}; \nМаксимальное число: {array[array_max]};')

min_max_sorted = sorted(array)
#print(min_max_sorted)
summary = 0
for i in range(min_max_sorted[0] + 1, min_max_sorted[-1]):
    summary = sum(min_max_sorted[1:-1])

print(f'Сумма элементов между минимальным и максимальным элементами массива равна {summary}')