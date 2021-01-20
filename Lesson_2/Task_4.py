# https://drive.google.com/file/d/1bVyup50ZfSsU4pG7dSRSYJc5G7TEkHTA/view?usp=sharing
# Задание 4 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сколько элементов сложить: '))
obj = 1
summary = 0
for i in range(n):
    summary += obj
    obj *= -0.5
print(f'Сумма n элементов равна - {summary}')