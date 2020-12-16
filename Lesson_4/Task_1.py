'''
Задание 1
Результаты анализа сохранить в виде комментариев в файле с кодом.

1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

'''

# Решение Задания 4 по уроку 2

#Вариант 1

# https://drive.google.com/file/d/1bVyup50ZfSsU4pG7dSRSYJc5G7TEkHTA/view?usp=sharing
# Задание 4 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

#n = int(input('Сколько элементов сложить: '))

def task_4_v1(n):
    obj = 1
    summary = 0
    for i in range(n):
        summary += obj
        obj *= -0.5
    print(f'Сумма n элементов равна - {summary}')




print(timeit.timeit('task_4_v1(10)', number=1000, globals=globals()))  # 0.0053528240000000026
print(timeit.timeit('task_4_v1(20)', number=1000, globals=globals())) #0.005649073999999921
print(timeit.timeit('task_4_v1(100)', number=1000, globals=globals()))  # 0.010556511000000005
print(timeit.timeit('task_4_v1(500)', number=1000, globals=globals()))  # 0.039238998
print(timeit.timeit('task_4_v1(1000)', number=1000, globals=globals()))  # 0.058858046
print(timeit.timeit('task_4_v1(10000)', number=1000, globals=globals()))  # 0.536590288
print(timeit.timeit('task_4_v1(100000)', number=1000, globals=globals()))  # 5.213581

cProfile.run('task_4_v1(10)')
        #1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        #1    0.000    0.000    0.000    0.000 Task_1.py:29(task_4_v1)
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('task_4_v1(100)')

        #1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        #1    0.000    0.000    0.000    0.000 Task_1.py:29(task_4_v1)
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




cProfile.run('task_4_v1(500)')

        #1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        #1    0.000    0.000    0.000    0.000 Task_1.py:29(task_4_v1)
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




cProfile.run('task_4_v1(1000)')
        #1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        #1    0.000    0.000    0.000    0.000 Task_1.py:29(task_4_v1)
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('task_4_v1(10000)')
        #1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        #1    0.001    0.001    0.001    0.001 Task_1.py:29(task_4_v1)
        #1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('='*80)

#Вариант 2


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




print(timeit.timeit('func_1(10)', number=1000, globals=globals())) #0.033819243
print(timeit.timeit('func_1(20)', number=1000, globals=globals())) #3.569106838
#print(timeit.timeit('func_1(30)', number=1000, globals=globals())) #не проходит

cProfile.run('func_1(10)')
        #1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #177/1    0.000    0.000    0.000    0.000 Task_1.py:104(func_1)
        #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_1(20)')
        #1    0.000    0.000    0.007    0.007 <string>:1(<module>)
  #21891/1    0.007    0.000    0.007    0.007 Task_1.py:104(func_1)
        #1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('func_1(50)')
        #Не проходит

print(f'=' * 80)
#Вариант 3
# Без диаграмы
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def vers_3(n, s=0, b=1):
    if n == 0:
        return s
    s += b
    n -= 1
    b /= 2
    return vers_3(n, s, b)

print(timeit.timeit('vers_3(10)', number=1000, globals=globals())) #0.0028468999999999994
print(timeit.timeit('vers_3(20)', number=1000, globals=globals())) #0.005260697999999998
print(timeit.timeit('vers_3(100)', number=1000, globals=globals())) #0.027017041999999998
print(timeit.timeit('vers_3(500)', number=1000, globals=globals())) #0.138455248
#print(timeit.timeit('vers_3(1000)', number=1000, globals=globals())) #0.033819243
#print(timeit.timeit('vers_3(10000)', number=1000, globals=globals())) #0.033819243
#print(timeit.timeit('vers_3(100000)', number=1000, globals=globals())) #0.

cProfile.run('vers_3(10)')
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  11/1    0.000    0.000    0.000    0.000 Test1.py:5(vers_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('vers_3(20)')

#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   21/1    0.000    0.000    0.000    0.000 Test1.py:5(vers_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('vers_3(100)')

#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 101/1    0.000    0.000    0.000    0.000 Test1.py:5(vers_3)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('vers_3(500)')

#    1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 501/1    0.000    0.000    0.000    0.000 Test1.py:5(vers_3)
#    1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




# Итоги
# Замеры проводил для n = 10, 100,500, 1000, 10000, 100000 ( и для n=20 из-за ограничений по рекурсии )
# В варианте 1 зависимость линейная ( не выраженная , т.к. при увеличении n на порядок ( * 10 ) при начальном кол-ве 10,
# время увеличивается в 2 раза, при след увеличении, приблизительно: [2;11;100;974]
# В варианте 2 решил задачу через и рекурсию, причем. очень криво( настоящий №:"%"код)) ) и видно, что зависимость в O(n!) :))
# Вариант 2 даже не запусился с n > 20
# Разница между вариантов 1 и 2: при n = 10 в 6 раз, при n = 20 в 631 раз ( !!!!).
# В варианте 3 построил более менее рекурсию. До n < 20 она выигрывает по скорости у варианта 1, но после заметно проседает.
# Основное ограничение n < 1000 должен быть.
# В зависимости от количества


#