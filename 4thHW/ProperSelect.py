# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random as rnd

def Randomizer(list):
    list = []
    for i in range(1, rnd.randint(2, 100)):
        list.append(rnd.randint(1, 50))
    return list

def Select(arg: list):
    arg.sort()
    i = 1
    while i <= len(arg) - 1:
        if arg[i - 1] == arg[i]:
            arg.remove(arg[i])
            i -= 1
        i += 1
    return arg

List = []
List = Randomizer(List)
List = Select(List)
print(List)