from tokenize import String
import Model

def ViewBook():
    with open(Model.init(), 'r', encoding='utf-8') as book:
        for line in book:
            print(line.rstrip('\n'))
        book.close()

def GetContactInfo():
        Data = Model.ReadFile()
        Need = input('Пожалуйста, введите ID контакта: ')
        for i in Data:
            String = i
            if Need in String[:2]:
                print(i)
                return
        print('Неверный ID, или ID который не существует')
        return
