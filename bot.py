import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def keys(message):
	key = types.ReplyKeyboardMarkup()
	key.row("Где учился?","Где работал?","Расскажи о себе", "Как с тобой связаться?")
	bot.send_message(message.chat.id, config.himsg, reply_markup=key)

@bot.message_handler(content_types=["text"])
def repeat(message):
	if message.text == "Где учился?":
		bot.send_message(message.chat.id, config.study)
	elif message.text == "Где работал?":
		bot.send_message(message.chat.id, config.work)
	elif message.text == "Расскажи о себе":
		bot.send_message(message.chat.id, config.about)
	elif message.text == "Как с тобой связаться?":
		bot.send_message(message.chat.id, config.contacts)
	else bot.send_message(message.chat.id, config.himsg, reply_markup=key)



if __name__ =='__main__':
	bot.polling(none_stop = True)