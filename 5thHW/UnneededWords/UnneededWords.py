# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def DeleteWords(path: str, arg: str):
    with open(path, 'r', encoding='utf-8') as read:
        data = read.read()
        data = data.replace(arg, '')
        data = data.replace(arg.lower(), '')
        data = data.replace(arg.upper(), '')
        read.close()
    path = 'file2.txt'
    file = open(path, 'w', encoding='utf-8')
    file.write(data)
    file.close

path = 'file.txt'
DeleteWords(path, 'абв')