# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Заметка: Данные придётся вводить самим

def Place(arg1, arg2, arg3):
    if arg1 < 0 or arg1 > 4:
        print("Invalid quarter")
    if arg2 < 0 or arg3 < 0:
        print("Invalid length for Ox or Oy")
    if arg1 == 1:
        print("The needed coordinate can be placed in Ox from 0 to ", arg2, " and in Oy from 0 to ", arg3)
    elif arg1 == 2:
        print("The needed coordinate can be placed in Ox from 0 to ", -arg2, " and in Oy from 0 to ", arg3)
    elif arg1 == 3:
        print("The needed coordinate can be placed in Ox from 0 to ", -arg2, " and in Oy from 0 to ", -arg3)
    elif arg1 == 4:
        print("The needed coordinate can be placed in Ox from 0 to ", arg2, " and in Oy from 0 to ", -arg3)

Quarter = int(input("Please, write a number of quarter: "))
x = int(input("Please, set the length for Ox: "))
y = int(input("Please, set the length for Oy: "))
Place(Quarter, x, y)
