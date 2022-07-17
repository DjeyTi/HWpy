# Реализуйте алгоритм перемешивания списка.
# Заметки: Можно было бы сделать через модуль random с функцией shufle, но на момент написания данной работы никто ещё не проходил
# модули, поэтому разберусь без данного модуля

def Shuffle(arg):
    if type(arg) != list:
        print("Invalid data")
        return
    for i in range(1, len(arg)//2 + 1):
        if i % 2 == 1:                                  
            arg[i - 1], arg[-i] = arg[-i], arg[i - 1]
    return arg

List = []
for i in range(1, 10):                                  # Не было сказано, какой диапазон списка. Беру 9 элементов
    List.append(i)
List = Shuffle(List)
print(List)