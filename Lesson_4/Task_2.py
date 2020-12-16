# Задание_2 Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile
import timeit


# Вариант 1 Решето Эратосфена
def sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result


# print(timeit.timeit('sieve(10)', number=1000, globals=globals())) #0.0028452510000000018
# print(timeit.timeit('sieve(100)', number=1000, globals=globals())) #0.021766471
# print(timeit.timeit('sieve(1000)', number=1000, globals=globals())) #0.23986699
# print(timeit.timeit('sieve(10000)', number=1000, globals=globals())) #2.730288878
# print(timeit.timeit('sieve(100000)', number=1000, globals=globals())) #29.856183119
cProfile.run('sieve(10)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 Test1.py:14(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Test1.py:5(sieve)
# 1    0.000    0.000    0.000    0.000 Test1.py:6(<listcomp>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve(100)')
#   1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#   1    0.000    0.000    0.000    0.000 Test1.py:14(<listcomp>)
#   1    0.000    0.000    0.000    0.000 Test1.py:5(sieve)
#   1    0.000    0.000    0.000    0.000 Test1.py:6(<listcomp>)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('sieve(1000)')

# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 Test1.py:14(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Test1.py:5(sieve)
# 1    0.000    0.000    0.000    0.000 Test1.py:6(<listcomp>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(10000)')

# 1    0.000    0.000    0.003    0.003 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 Test1.py:14(<listcomp>)
# 1    0.002    0.002    0.003    0.003 Test1.py:5(sieve)
# 1    0.000    0.000    0.000    0.000 Test1.py:6(<listcomp>)
# 1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(100000)')


#   1    0.001    0.001    0.037    0.037 <string>:1(<module>)
#   1    0.003    0.003    0.003    0.003 Test1.py:14(<listcomp>)
#   1    0.029    0.029    0.037    0.037 Test1.py:5(sieve)
#   1    0.005    0.005    0.005    0.005 Test1.py:6(<listcomp>)
#   1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(f'='*80)
# Вариант 2

def prime(n):
    n = int(n)
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


# print(timeit.timeit('prime(10)', number=1000, globals=globals())) #0.0015782730000000016
# print(timeit.timeit('prime(100)', number=1000, globals=globals())) #0.018541803
# print(timeit.timeit('prime(1000)', number=1000, globals=globals())) #0.268351099
# print(timeit.timeit('prime(10000)', number=1000, globals=globals())) #3.8948959289999996
# print(timeit.timeit('prime(100000)', number=1000, globals=globals())) #71.35127177700001
cProfile.run('prime(10)')
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 Test1.py:5(prime)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(100)')
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 Test1.py:5(prime)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(1000)')
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 Test1.py:5(prime)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  167    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(10000)')
#  1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#  1    0.005    0.005    0.005    0.005 Test1.py:5(prime)
#  1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#  1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(100000)')
#  1    0.000    0.000    0.074    0.074 <string>:1(<module>)
#  1    0.073    0.073    0.073    0.073 Test1.py:5(prime)
#  1    0.000    0.000    0.074    0.074 {built-in method builtins.exec}
#  9591    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Итоги
# В схожих задач где n < 100 лучше использовать функцию prime
# При n > 100 лучше использовать функцию sieve ( Решето Эратосфена )

