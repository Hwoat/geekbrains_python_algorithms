#   https://app.diagrams.net/#G1bVyup50ZfSsU4pG7dSRSYJc5G7TEkHTA
# Задание 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input("Введите целое число: "))
even = 0
uneven = 0

while num > 0:
    if num % 10 % 2 == 0:
        even += 1
    else:
        uneven += 1
    num = num // 10
print(f"Кол-во четных цифр - {even}, нечетных цифр - {uneven}")
