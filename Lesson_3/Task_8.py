# Задание 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []
rows = 5
columns = 3
# 4 - 1

for i in range(rows):
    row = []
    summary = 0

    for k in range(columns):
        num = int(input(f'{i+1}-я строка, {k+1}-й столбец : '))
        summary += num
        row.append(num)

    #line_text.append(i+1)
    row.append(summary)
    matrix.append(row)
#line_num = 0

print(f'Матрица. Решение')
for line in matrix:
    #line_num += 1
    #print(f'{line_num}-я cтрока {line}')
    print(f'{line}')
