Path = 'HW/8thHW/file.txt'

def init():
    global Path
    return Path

def ReadFile():
    with open(init(), 'r', encoding='utf-8') as book:
        Data = book.readlines()
        book.close()
    return Data

def NewAccount():
    Data = ReadFile()
    with open(init(), 'a', encoding='utf-8') as book:
        NewAccount = f"\n{len(Data)}, {input('Пожалуйста, введите по примеру (ФИО, Номер):')}"
        book.writelines(NewAccount)
        book.close()

def ClearBook():
    with open(init(), 'w', encoding='utf-8') as book:
        book.write('ID, ФИО, Номер')
        book.close