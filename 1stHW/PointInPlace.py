# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Заметка: Данные вводим сами

def Place(arg1, arg2):
    if type(arg1) != int or type(arg2) != int:
        print("Writen coordinates are not valid")
    if arg1 == 0 or arg2 == 0:
        print("Writen coordinates are not valid")
    if arg1 > 0 and arg2 > 0:
        print("1st quarter")
    elif arg1 < 0 and arg2 > 0:
        print("2nd quarter")
    elif arg1 < 0 and arg2 < 0:
        print("3rd quarter")
    elif arg1 > 0 and arg2 < 0:
        print("4th quarter") 

x = int(input("Please, write the coordinate for X: "))
y = int(input("Please, write tht coordinate for Y: "))
Place(x, y)