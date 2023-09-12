import telebot

from telebot import types

botTimeWeb = telebot.TeleBot('6565999957:AAE3PMeIqsbmWd4_bG5aqCBYQNhh0GPMsk4')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь покажу мега видео?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.data == "yes":
        video = open('video.mp4', 'rb')
        botTimeWeb.send_video(function_call.message.chat.id, video)


botTimeWeb.infinity_polling(timeout=2000)