# Задание 1
# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company_cnt = int(input('Введите кол-во предприятий: '))
companies = []
companies_above = []
companies_below = []
companies_eq = []
profit_all = 0

Company = namedtuple('Company', ['name', 'profit'])

for i in range(company_cnt):
    name = input(f'Название {i + 1}-й компании: ')
    profit = sum([float(input(f'Прибыль компании за {j}-й квартал: ')) for j in '1234'])
    profit_all += profit
    c = Company(name, profit)
    companies.append(c)

profit_all_avg = profit_all / company_cnt

for c in companies:
    if c.profit < profit_all_avg:
        companies_below.append(c)
    elif c.profit > profit_all_avg:
        companies_above.append(c)
    else:
        companies_eq.append(c)

print()
print(f'Средняя прибыль за год по всем компаниям: {profit_all_avg:.2f}')

if companies_above:
    print(f'Компании с прибылью выше средней:')
    for c in companies_above:
        print(f'{c.name}: {c.profit:.2f}')
    print()

if companies_eq:
    print(f'Компании с прибылью равной средней:')
    for c in companies_eq:
        print(f'{c.name}: {c.profit:.2f}')
    print()

if companies_below:
    print(f'Компании с прибылью ниже средней:')
    for c in companies_below:
        print(f'{c.name}: {c.profit:.2f}')