import telegram
import requests
import json
from telegram import Update
from time import sleep
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler, MessageHandler, Filters, ConversationHandler
from telegram.chataction import ChatAction
from telegram.bot import Bot
from telegram.update import Update

# secrets=json.load(open('bot_token.json'))
# updater = Updater(secrets['token'], use_context=True)
Updater =Updater(token, use_context=True)
def start(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    update.message.reply_text('Hi\nThis Bot is developed by APD🌷\nTo Know the commands in this Bot🤖 enter /help')

def help(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    update.message.reply_text('This Bot uses following commands\n/hello\n/help\n/shorturl - Shortens a long URL to short Url')

def hello(update: Update, context: CallbackContext) -> None:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def short_url (update: Update, context: CallbackContext):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    url_json={'url':update['message']['text']}
    short_url=requests.post('https://cleanuri.com/api/v1/shorten',url_json)
    if short_url.status_code==200:
        update.message.reply_text(short_url.json()['result_url'])
    else:
        update.message.reply_text(short_url.json()['error']+"\nerror code:"+str(short_url.status_code))
    return ConversationHandler.END

def short_url_callback(update: Update, context: CallbackContext) :
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    update.message.reply_text('Enter the long URL to be shorten\nEnter /cancel to cancel')
    telegram.ForceReply(force_reply=True)
    return 'SHURL' 

def cancel (update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Process is canceled succesfuly👍\nTry other commands as well')
    return ConversationHandler.END

short_url_conv= ConversationHandler(
    entry_points=[CommandHandler('shorturl', short_url_callback)],
    states={
        'SHURL':[MessageHandler(Filters.text& ~Filters.command,short_url) ]
    },
    fallbacks=[CommandHandler('cancel',cancel)]
)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(short_url_conv)

updater.start_polling()
updater.idle()