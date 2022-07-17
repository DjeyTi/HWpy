# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def Multiplicate(arg):
    if type(arg) != int and type(arg) != float:
        print("Invalid data")
    i = 0
    Mult = 1
    for i in range(1, arg + 1):
        Mult = Mult * i
        print(Mult)

x = 5
Multiplicate(x)
