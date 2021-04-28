"""
</>
Date: 04.27.2021
Time: 6:00 PM
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Cyrill - Latin Telegram Bot"
</>
"""
import telegram
from telegram import Update, update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from transliterate import transliterate, check

def do_something(user_input):
    check_type = check(user_input)
    answer = transliterate(user_input,check_type)
    return answer

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(do_something(user_input))


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Assalomu alaykum, {update.effective_user.first_name}")


updater = Updater('Token for the HTTP API')

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))


updater.start_polling()
updater.idle()