from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Model import init, ReadFile

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Добро, {update.effective_user.first_name}')

def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('HW/10thHW/TeleBot/log.md', 'a')
    file.write(f'\n{update.effective_user.id}, {update.message.text}')
    file.close()
    msg = update.message.text
    items = msg.split()
    if items[2] == '+':
        answer = float(items[1]) + float(items[3])
    elif items[2] == '-':
        answer = float(items[1]) - float(items[3])
    elif items[2] == '/':
        answer = float(items[1]) / float(items[3])
    elif items[2] == '*':
        answer = float(items[1]) * float(items[3])
    else:
        return
    return update.message.reply_text(f'Ответ - {answer}')

async def ViewBook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(init(), 'r', encoding='utf-8') as book:
        for line in book:
            await update.message.reply_text(f'{line}')
            print(line.rstrip('\n'))
        book.close()

async def NewAccount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Data = ReadFile()
    msg = update.message.text
    items = msg.split()
    with open(init(), 'a', encoding='utf-8') as book:
        NewAccount = f"\n{len(Data)}, {items[1]} {items[2]}"
        book.writelines(NewAccount)
        book.close()
    await update.message.reply_text('Аккаунт создан')

async def ClearBook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(init(), 'w', encoding='utf-8') as book:
        book.write('ID, ФИО, Номер')
        book.close
    await update.message.reply_text('Список контактов очищен')    

async def Help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello \n/calculate "x (+, -, /, *) y" \n/newaccount "Имя, номер телефона" \n/checkinfo \n/clearbook \n/getcontact "ID"')

async def GetContactInfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Data = ReadFile()
    msg = update.message.text
    Need = msg.split()
    for i in Data:
        String = i.split()
        String[0].replace(',', '')
        if Need[1] in String[0]:
            await update.message.reply_text(i)
