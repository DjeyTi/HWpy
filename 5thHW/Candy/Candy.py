# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Заметка: Я не вижу никаких входных/выходных данных, которые должны быть выведены в текстовом формате. Если это не так, я переделаю.

import random as rnd

def CandyGame():
    Candy = 2021
    FirstPlay = rnd.randint(1,2)
    if FirstPlay == 1:
        PlayerTurn = True
        print("Первый ход за Игроком")
    else:
        PlayerTurn = False
        print("Первый ход за Володей(Бот)")
    while Candy > 0:
        if PlayerTurn:
            print("Ход Игрока")
            while PlayerTurn == True:
                Take = int(input("Пожалуйста, возьмите до 28 конфет из чаши: "))
                if 0 < Take < 29:
                    PlayerTurn = False
                else:
                    print("Пожалуйста, введите корретное количество конфет")
            Candy -= Take
            print(f"В чаше {Candy} конфеток")
        if Candy <= 0:
            print("Игрок победил, все конфеты уходят ему")
            return
        if PlayerTurn != True:
            print("Ход Володи")
            if Candy <= 28:
                print(f"Володя взял {Candy} конфет")
                Candy -= Candy
                print(f"В чаше {Candy} конфеток")
                print("Володя победил, все конфеты уходят ему")
                return
            if 29 < Candy <= 57 and Candy != 29:
                print(f"Володя взял {Candy - 29} конфет")
                Candy = Candy - (Candy - 29)
            else:
                Take = rnd.randint(1, 28)
                print(f"Володя взял {Take} конфет")
                Candy -= Take
            PlayerTurn = True
        print(f"В чаше {Candy} конфеток")
        
CandyGame()