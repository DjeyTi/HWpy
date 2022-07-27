# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def Multiplication(arg: list):
    List = []
    i = 0
    while i < len(arg) / 2:
        List.append(arg[i] * arg[len(arg) - 1 - i])
        i += 1
    return List

List = [5, 8, 2, 9, 4]
print(Multiplication(List))