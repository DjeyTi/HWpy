Path = 'HW/10thHW/TeleBot/file.txt'

def init():
    global Path
    return Path

def ReadFile():
    with open(init(), 'r', encoding='utf-8') as book:
        Data = book.readlines()
        book.close()
    return Data