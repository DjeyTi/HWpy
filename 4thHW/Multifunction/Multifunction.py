# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

from pathlib import Path
import random as rnd

def Multifunctional(arg):
    path = Path('JustAFile.txt')
    file = open(path, 'w')
    for i in range(0, arg + 1):
        if i == 0:
            file.writelines(f"{rnd.randint(0, 100)} + ")
        if 0 < i < arg:
            file.writelines(f"{rnd.randint(0, 100)} * k^{i} + ")
        if i == arg:
            file.writelines(f"{rnd.randint(0, 100)} * k^{i} = 0")
    file.close

k = rnd.randint(2, 5)
Multifunctional(k)

# Заметка напоследок: Пытался придумать способ добавления файла в саму папку, пока не доудмался, в будущем я додумаю, 
# как это можно сделать. А так задача выполнена.