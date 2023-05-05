# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
""" def power(a,b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a,-b)
    if b % 2 == 0:
        return power(a,b//2) * power(a,b//2) 
    else:
        return power(a,b-1) * a

a = int(input())
b = int(input())
print(power(a,b)) """

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ(a, b):
    if a >= 0 and b >= 0:
        if b == 0:
            return a
        return summ(a+1,b-1)

a = int(input())
b = int(input())
print(summ(a,b))