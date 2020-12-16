# https://drive.google.com/file/d/1bVyup50ZfSsU4pG7dSRSYJc5G7TEkHTA/view?usp=sharing
# Задание 3 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

num = int(input("Введите целое число: "))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(f" Выверрнутое число - {result}")