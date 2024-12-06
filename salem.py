import telebot

bot = telebot.TeleBot("7850029728:AAGMYdzbv15FKkptWQsuzlhzquFiLhXX-_A")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "всем привет, добро пожаловать в магазин salem")

bot.polling(none_stop=True, interval=0)

