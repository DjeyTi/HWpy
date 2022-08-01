# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random as rnd

def Randomizer(List):
    List = [i for i in range(1, rnd.randint(2, 100))]
    return list(map(lambda i: rnd.randint(1, 50), List))

def Select(arg: list):
    arg.sort()
    return list(set(arg))

List = []
List = Randomizer(List)
List = Select(List)
print(List)