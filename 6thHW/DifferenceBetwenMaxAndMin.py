# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Заметка: В задаче ненаписана точность дробной части, поэтому буду придерживаться точности d = 1e-2

def Difference(arg: list):
    d = 2
    arg = list(map(lambda i: i % 1, arg))
    return round(max(arg), d) - round(min(arg), d)


List = [1.01, 2.17, 3.89, 4.68, 5.02]
print(Difference(List))