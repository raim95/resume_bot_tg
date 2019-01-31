
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

updater = Updater(token='642035956:AAG5VuVk81SI_McYQRhXvjAZipdJTeaUVHQ')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, меня зовут Альтрон.')

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
		bot.send_message(chat_id=update.message.chat_id, text='Do not undestand')

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)


dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)


updater.start_polling(clean=True)


updater.idle()
