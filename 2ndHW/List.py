# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся через пробел пользователем.

def FromStrToInt(arg):
    arg = arg.split()
    NewArg = []
    for i in arg:
        NewArg.append(int(i))
    return NewArg

def Multiplication(arg):
    arg = FromStrToInt(arg)
    if type(arg) != list:
        print("Invalid data")
        return
    N = 5
    List = []
    for i in range(-N, N, 2):           # Не было никаких предложений, какими имено числами заполнять промежуток
        List.append(i)                  # Буду заполнять перескакивая значения
    print(List)
    return List[arg[0] - 1] * List[arg[1] - 1]

X = input()
X = Multiplication(X)
print(X)