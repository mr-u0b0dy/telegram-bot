# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# bot = telegram.bot(token='') 
# updater = Updater(token='', use_context=True) 
# dispatcher = updater.dispatcher
# def hello(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
# hello_handler = CommandHandler('hello', hello)
# dispatcher.add_handler(hello_handler)
# updater.start_polling()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('1843979701:AAFFJ2T1Cy-Y6D2Ab5DPoAPlB_su8uJrVCQ')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()