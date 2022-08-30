from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Model import init, ReadFile

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

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
    return update.message.reply_text(f'The answer is {answer}')

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
        NewAccount = f"\n{len(Data)}, {items[1]}, {items[2]}"
        book.writelines(NewAccount)
        book.close()
    await update.message.reply_text('New Account Created')

async def ClearBook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(init(), 'w', encoding='utf-8') as book:
        book.write('ID, ФИО, Номер')
        book.close
    await update.message.reply_text('Book cleared')    
