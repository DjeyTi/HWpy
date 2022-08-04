# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# Создание нового аккаунта в справочнике
def NewAcc(path):
    with open(path, 'r', encoding='utf-8') as book:
        data = book.readlines()
        book.close()
    with open(path, 'a', encoding='utf-8') as book:
        NewAccount = f"\n{len(data) - 1}, {input('Пожалуйста, введите по примеру (ФИО, Номер):')} "
        book.writelines(NewAccount)
        book.close()

# Просмотр справочника
def GetInfo(path):
    with open(path, 'r', encoding='utf-8') as book:
        for line in book:
            print(line.rstrip('\n'))
        book.close()

# Вывод информации нужного контакта из справочника
def GetContact(path):
    with open(path, 'r', encoding='utf-8') as book:
        data = book.read()
        data = data.split('\n')
        Tuple = {}
        for i in range(1, len(data)):
            Tuple[i] = data[i].split(', ')
        book.close()
    return Tuple[int(input('Пожалуйста, введите ID нужного вам контакта: '))]

path = 'file.txt'

