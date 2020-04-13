import telebot
from telebot import apihelper
from telebot import types


bot = telebot.TeleBot('666185661:AAGeoxYjRX4eednqACEWixlaIhjSTZK3GXk')
apihelper.proxy = {
    'https': 'socks5h://67.205.149.230:1080',
}
but = types.ReplyKeyboardMarkup(row_width=2)

user_info = bot.get_me()
button = types.KeyboardButton('Smoke 10 min')
button1 = types.KeyboardButton('Smoke 20 min')
but.add(button, button1)

updates = bot.get_updates()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "HII":
        bot.send_message(message.from_user.id, "Hello", reply_markup=but)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "WTF")
    else:
        bot.send_message(message.from_user.id, "FUCK /help.")


bot.polling(none_stop=True, interval=0)

