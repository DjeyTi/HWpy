# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonachi(arg):
    List = [1, -1]
    i = 1
    NewList = []
    while i < arg - 1:
        List.append(List[i - 1] - List[i])
        i += 1
    i = arg - 1
    while i >= 0:
        NewList.append(List[i])
        i -= 1
    NewList.append(0)
    i = arg
    while i < arg + arg:
        NewList.append(NewList[i - 1] + NewList[i])
        i += 1
    print(NewList)
    
    
Fibonachi(10)