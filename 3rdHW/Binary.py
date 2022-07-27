# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def Binary(arg):
    i = 0
    Bi = 0
    while arg > 1:
        Bi = Bi + (arg % 2 * 10**i)
        print(Bi)
        i += 1
        arg //= 2
    Bi = Bi + (arg * 10**(i))
    return Bi

print(Binary(136))