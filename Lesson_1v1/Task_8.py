# https://drive.google.com/file/d/1NWk2_6zZ3gyL53t24JZh63CB_urA08O3/view?usp=sharing

# Задача 8 Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input("Введите год в формате ХХХХ: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Високосный")
        else:
            print(f"Обычный")
    else:
        print(f"Висоскосный")
else:
    print(f"Обычный")


