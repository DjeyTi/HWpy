import View
import Model

def MainProgram():
    print('Добро пожаловать, что вы желаете сделать с вашим справочником: \na - Добавить новый контакт\nd - Очистить справочник')
    print('v - Посмотреть справочник\nc - Посмотреть контакт\nq - Закрыть программу')
    Choice = input()
    if Choice.lower() == 'a':
        Model.NewAccount()
        print('Контакт добавлен')
        return MainProgram()
    elif Choice.lower() == 'd':
        SecondChoice = input('Вы уверены в своих действиях? y - да, n - нет: ')
        if SecondChoice.lower() == 'y':
            Model.ClearBook()
            print('Справочник очищен')
            return MainProgram()
        elif SecondChoice.lower() == 'n':
            print('Возврат в главное меню...')
            return MainProgram()
        else:
            print('Неверная команда. Возврат в главное меню...')
            return MainProgram()
    elif Choice.lower() == 'v':
        View.ViewBook()
        return MainProgram()
    elif Choice.lower() == 'c':
        View.GetContactInfo()
        return MainProgram()
    elif Choice.lower() == 'q':
        print('Закрытие программы')
        return
    else:
        print('Неверная команда')
        return MainProgram()
        
        