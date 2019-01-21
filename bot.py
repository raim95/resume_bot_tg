# -*- config: utf-8 -*-
import config
import telebot
import os
import time

bot = telebot.TeleBot(config.token)

#@bot.message_handler(content_types=["text"])
#def repeat(message):
#	bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['pic'])
def find_file_ids(message):
	for file in os.listdir('pic/'):
		if file.split('.')[-1]=='ogg':
			f = open ('pic/'+file, 'rb')
			msg = bot.send_photo(message.chat.id, f, None)
			bot.send_message(message,chat.id, msg.photo.file_id, reply_to_message_id=msg.message_id)
		time.sleep(3)

if __name__ =='__main__':
	bot.polling(none_stop = True)