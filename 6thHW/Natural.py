# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import random as rnd

def Natural(arg):
    list = [i for i in range(2, arg + 1) if arg % i == 0]
    print(F"Added argument {arg} have next numbers, that gives 0 in process of division: {list}")

x = rnd.randint(2, 100)
Natural(x)
