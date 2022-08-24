import model

def MainProgram():
    print("Добро пожалоать, чего изволите?")
    print("DV - Скачать видео")
    answer = input('Ожидается команда: ')
    if answer == 'DV':
        model.GetVideo(input('Введите сылку: '))
        return MainProgram()
    elif answer == 'Q':
        return
    else:
        print('Неверная команда, возврат в главное меню')
        return MainProgram()
        
MainProgram()