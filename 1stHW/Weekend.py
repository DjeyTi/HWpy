# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Заметка: Число вводим сами

def IsItWeekend(arg):
    if arg == 6 or arg == 7:
        print("Yes")
    else:
        print("No")

IsItWeekend(int(input("Please, enter number of day of the week ")))