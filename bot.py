# -*- config: utf-8 -*-
import config
import random
import telebot
import os
import time
from random import shuffle
import utils
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['pic'])
def find_file_ids(message):
	file = open('files_id.txt', 'w')
	file.close()
	for file in os.listdir('pic/'):
		if file.split('.')[-1]=='jpg':
			f = open ('pic/'+file, 'rb')
			msg = bot.send_photo(message.chat.id, f)
			bot.send_message(message.chat.id, msg.photo[0].file_id, reply_to_message_id=msg.message_id)
			file_id = msg.photo[0].file_id
			f = open('files_id.txt', 'a')
			f.write(file_id +'\n')
			f.close()
		time.sleep(3)
		
@bot.message_handler(commands=['game'])
def game(message):
    # Подключаемся к БД
    db_worker = SQLighter(config.database_name)
    # Получаем случайную строку из БД
    row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    # Формируем разметку
    markup = utils.generate_markup(row[2], row[3])
    # Отправляем аудиофайл с вариантами ответа
    bot.send_voice(message.chat.id, row[1], reply_markup=markup)
    # Включаем "игровой режим"
    utils.set_user_game(message.chat.id, row[2])
    # Отсоединяемся от БД
    db_worker.close()
	

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    # Если функция возвращает None -> Человек не в игре
    answer = utils.get_answer_for_user(message.chat.id)
    # Как Вы помните, answer может быть либо текст, либо None
    # Если None:
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
    else:
        # Уберем клавиатуру с вариантами ответа.
        keyboard_hider = types.ReplyKeyboardRemove()
        # Если ответ правильный/неправильный
        if message.text == answer:
            bot.send_message(message.chat.id, 'Верно!', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Увы, Вы не угадали. Попробуйте ещё раз!', reply_markup=keyboard_hider)
        # Удаляем юзера из хранилища (игра закончена)
        utils.finish_user_game(message.chat.id)

if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)