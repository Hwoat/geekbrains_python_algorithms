# https://drive.google.com/file/d/1bVyup50ZfSsU4pG7dSRSYJc5G7TEkHTA/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
def func_1(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return (func_1(x - 1) * 0.5) + (func_1(x - 2) * 0.5)


x = int(input("Введите натуральное число: "))
print(f'Сумма элементов -  {func_1(x)}')