import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def keys(message):
	key = types.ReplyKeyboardMarkup()
	key.row("1","2","3")
	bot.send_message(message.chat.id, "Выберите цифру:", reply_markup=key)

@bot.message_handler(content_types=["text"])
def repeat(message):
	bot.send_message(message.chat.id, "Здравствуйте! Я бот-резюме. Узнать некоторые факты обо мне ты сможешь с помощью меню внизу. Если ты потерял меню, оно откроется по нажатию иконки из квадратиков возле значка камеры.")



if __name__ =='__main__':
	bot.polling(none_stop = True)