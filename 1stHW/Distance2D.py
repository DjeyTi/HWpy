# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Заметка для себя: Теорема Пифагора с катетами 3 и 4

def Dist(arg1, arg2):
    if type(arg1) != list or type(arg2) != list:
        print("Invalid type of data")
    FirstSide = arg1[0] - arg2[0]
    SecondSide = arg1[1] - arg2[1]
    Answer = (FirstSide**2 + SecondSide**2)**0.5
    return Answer

A = [5, 15]
B = [2, 19]
print(Dist(A, B))