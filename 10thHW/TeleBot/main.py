from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import BotCommand

app = ApplicationBuilder().token("Введите сюда токен бота").build()

app.add_handler(CommandHandler("hello", BotCommand.hello))
app.add_handler(CommandHandler("calculate", BotCommand.calculate))
app.add_handler(CommandHandler("newaccount", BotCommand.NewAccount))
app.add_handler(CommandHandler("checkinfo", BotCommand.ViewBook))
app.add_handler(CommandHandler("clearbook", BotCommand.ClearBook))
print('Server start')
app.run_polling()