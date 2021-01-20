
# Задание 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = int(input("Введите количество элементов массива: "))
array = [random.randint(-100, 100) for _ in range(size)]

array_min = 0
array_max = 0

print(f'Исходный массив:\n\t{array}')

for i in range(len(array)):
    if array[i] < array[array_min]:
        array_min = i
    elif array[i] > array[array_max]:
        array_max = i

array[array_min], array[array_max] = array[array_max], array[array_min]
print(f'Изменённый массив:\n\t{array}')