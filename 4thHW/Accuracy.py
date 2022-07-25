# Вычислить число c заданной точностью d (?)
# Не совсем понимаю, почему именно d

import random as rnd

def Accuracy(arg):
    d = rnd.randrange(1, 10, 1)
    Answer = round(arg, d)
    d = 10 ** -d
    print("Accuracy of this number is ", d, " number's")
    return Answer

pi = 3.14159265358979
print(Accuracy(pi))