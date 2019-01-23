import config
import telebot
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

updater = Updater(token=config.token)
bot = telebot.TeleBot(config.token)
dispatcher = updater.dispatcher

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

def textMessage(bot, update):
    request = apiai.ApiAI('d19ec966a8314d22bacbe59da0dfc2a4').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot' 
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')

dispatcher.add_handler(text_message_handler)

if __name__ =='__main__':
	bot.polling(none_stop = True)