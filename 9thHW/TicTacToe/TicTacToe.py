import random as rnd

def TicTacToe():
    path = 'HW\9thHW\TicTacToe\TicTacToe.txt'
    with open(path, 'r', encoding='utf-8') as read:
        data = read.read()              # Местоположение чисел - 0 4 8 20 24 28 40 44 48
        print(data)
        PlayerTurn = True
        Answer = False
        GameIsOn = True
        List = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while GameIsOn:
            if PlayerTurn:
                Answer = False
                Input = input("Выберите позицию, показанную на сетке: ")
                for i in List:
                    if i == Input:
                        List.remove(i)
                        Answer = True
                if Answer:
                    data = data.replace(Input, 'x')
                    PlayerTurn = False
                    print(data)
                    if data[0] == data[4] == data[8] or data[20] == data[24] == data[28] or data[40] == data[44] == data[48]:
                        print("Игрок победил")
                        return
                    if data[0] == data[20] == data[40] or data[4] == data[24] == data[44] or data[8] == data[28] == data[48]:
                        print("Игрок победил")
                        return
                    if data[0] == data[24] == data[48] or data[8] == data[24] == data[40]:
                        print("Игрок победил")
                        return
                    Check = False
                    if List != []:
                        Check = True
                    if Check != True:
                        print("Конец игры, нет возможных ходов")
                        return
                elif Answer != True:
                    print("Неверная позиция, введите ещё раз")
                print('')
            else:
                Answer = False
                Input = str(rnd.randint(1, 9))
                for i in List:
                    if i == Input:
                        List.remove(i)
                        Answer = True
                if Answer:
                    data = data.replace(Input, 'o')
                    PlayerTurn = True
                    print(data)
                    if data[0] == data[4] == data[8] or data[20] == data[24] == data[28] or data[40] == data[44] == data[48]:
                        print("Бот победил")
                        return
                    if data[0] == data[20] == data[40] or data[4] == data[24] == data[44] or data[8] == data[28] == data[48]:
                        print("Игрок победил")
                        return
                    if data[0] == data[24] == data[48] or data[8] == data[24] == data[40]:
                        print("Бот победил")
                        return

TicTacToe()

# Заметки: Либо я чего-то не понимаю, либо VEnv не желает работатьна VSC. Окружение создано, но оно не желает открываться в VSC.
# Пакеты все нужные уже имеются там, поэтому не думаю, что работа этой задачи как-то будет изменена, поэтому если нужно будет додумать, что не так с VSC, додумаю позже.