# Задайте список из n чисел последовательности (1 + 1/n)^n(?) и выведите на экран их сумму(?).
# Заметки: Данная функция не выведет значения, которые были в примере, также сумму чего, не совсем понятно -
# сумму последовательности или сумму чисел последовательностей

def Func(arg):
    if type(arg) != int and type(arg) != float:
        print("Invalid data")
    for i in range(1, arg + 1):
        Answer = (1 + (1/i))**i # Заметка при тестировании: при int((1 + (1/i))**i) будут одни лишь двойки
        print(Answer)

x = 10
Func(x)

# Задача вроде как выполнена, но не так, как показана была на примере выполнения, если будут замечания
# я их учту при перевыполнений этой задачи, а пока оставляю так