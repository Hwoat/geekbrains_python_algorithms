# https://drive.google.com/file/d/1NWk2_6zZ3gyL53t24JZh63CB_urA08O3/view?usp=sharing
# Задача 9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
c = int(input("Введите 3-ое число: "))

if b < a < c or c < a < b:
    print(f'Среднее = {a}')
elif a < b < c or c < b < a:
    print(f'Среднее = {b}')
else:
    print(f'Среднее = {c}')