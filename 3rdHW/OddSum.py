# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def OddSum(arg: list):
    Sum = 0
    for i in range(1, len(arg), 2):
        Sum += arg[i]
    return Sum

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(OddSum(List))