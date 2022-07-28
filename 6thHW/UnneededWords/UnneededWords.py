# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def DeleteWords(path: str, arg: str):
    path = 'file.txt'
    with open(path, 'r', encoding='utf-8') as read:
        data = read.read()
        data = data.replace(arg, '')
        data = data.replace(arg.lower(), '')
        data = data.replace(arg.upper(), '')
        print(data)

path = 'file.txt'
DeleteWords(path, 'абв')