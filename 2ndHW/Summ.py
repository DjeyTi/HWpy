# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def GetSum(arg):
    if type(arg) != int and type(arg) != float:
        print("Invalid data, type of data is ", type(arg))
    while arg % 1 != 0:
        arg *= 10
    Sum = 0
    while arg >= 10:
        Sum = Sum + arg % 10
        arg = arg // 10
    Sum = int(Sum + arg)
    print(Sum)

x = 0.123

GetSum(x)
