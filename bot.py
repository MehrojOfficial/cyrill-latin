"""
</>
Date: 04.27.2021
Time: 6:00 PM
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Cyrill - Latin Telegram Bot"
</>
"""
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from transliterate import transliterate

status = ''

def latin_cyrill(user_input):
    answer = transliterate(user_input,'cyrillic')
    return answer

def cyrill_latin(user_input):
    answer = transliterate(user_input, 'latin')
    return answer

def none_status():
    answer = 'Hurmatli foydalanuvchi. Botdan foydalanishdan avval yo\'nalishni sozlab oling.\nLotin - Kiril | /lotin_kiril \nKiril - Lotin | /kiril_lotin'
    answer += '\n\nҲурматли фойдаланувчи. Ботдан фойдаланишдан аввал йўналишни созлаб олинг.\nЛотин - Кирил | /lotin_kiril \nКирил - Лотин | /kiril_lotin'
    return answer

def reply(update, context):
    user_input = update.message.text
    if status == 'latin_cyrill':
        update.message.reply_text(latin_cyrill(user_input))
    elif status == 'cyrill-latin':
        update.message.reply_text(cyrill_latin(user_input))
    elif status == '':
        update.message.reply_text(none_status())


def status1(update: Update, context: CallbackContext):
    global status
    status = 'latin_cyrill'
    update.message.reply_text("Йўналиш Лотин - Кирил қилиб созланди.\n\nҚайта созлаш: /help")

def status2(update: Update, context: CallbackContext):
    global status
    status = 'cyrill-latin'
    update.message.reply_text("Yo'nalish Kiril - Lotin qilib sozlandi.\n\nQayta sozlash: /help")

<<<<<<< HEAD

def help(update: Update, context: CallbackContext):
    if status == 'latin_cyrill':
        answer = "Бу бот сизга матнларни Лотинда Кирилга ва тескарисига бехато ўгиришда ёрдам беради."
        answer += "\nФойдали буйруқлар:\nЛотин - Кирил | /lotin_kiril \nКирил - Лотин | /kiril_lotin"
    elif status == 'cyrill-latin':
        answer = "Bu bot sizga matnlarni Lotinda Kirilga va teskarisiga bexato o'girishda yordam beradi."
        answer += "\nFoydali buyruqlar:\nLotin - Kiril | /lotin_kiril \nKiril - Lotin | /kiril_lotin"
    elif status == '':
        answer = "Bu bot sizga matnlarni Lotinda Kirilga va teskarisiga bexato o'girishda yordam beradi."
        answer += "\nFoydali buyruqlar:\nLotin - Kiril | /lotin_kiril \nKiril - Lotin | /kiril_lotin"
        answer += "\n\nБу бот сизга матнларни Лотинда Кирилга ва тескарисига бехато ўгиришда ёрдам беради."
        answer += "\nФойдали буйруқлар:\nЛотин - Кирил | /lotin_kiril \nКирил - Лотин | /kiril_lotin"
    update.message.reply_text(answer)

def hello(update: Update, context: CallbackContext) -> None:
    answer = f"Assalomu alaykum, {update.effective_user.first_name}"
    answer += "\nBotdan foydalanishni boshlashdan avval uni sozlab oling: /help"
    update.message.reply_text(answer)

=======
>>>>>>> parent of cb772e9 (Update bot.py)
updater = Updater('1763522327:AAEySG3ilGrnyOVWmk23szF-c1Ad27O2zHA')

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('lotin_kiril', status1))
updater.dispatcher.add_handler(CommandHandler('kiril_lotin', status2))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
