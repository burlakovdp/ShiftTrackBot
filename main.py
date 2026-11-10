import telebot
from telebot import types
from config import TOKEN

import utils as hs
from managers import *
import database

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

chat_data = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def menu(message):
    chat_id = message.chat.id
    user = UserManager()
    chat_data[chat_id] = user
    user.add_data('stage', hs.Stack())
    user.push_stage('menu_stage')
    user.add_data('language', 'eng')
    user.add_user_id(message.from_user.id)
    user.print_stage()
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(),
                                                user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.back_manager(chat_data[message.chat.id].get_stage(),
                                                          message.text, chat_data[message.chat.id].get_language()))
def back(message):
    chat_id = message.chat.id
    chat_data[chat_id] = user
    user.pop_stage()
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.cancel_manager(chat_data[message.chat.id].get_stage(),
                                                            message.text, chat_data[message.chat.id].get_language()))
def cancel(message):
    chat_id = message.chat.id
    chat_data[chat_id] = user
    while user.get_size() > 1:
        user.pop_stage()
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'resume_stage',
                                                           chat_data[message.chat.id].get_language()))
def resume(message):
    chat_id = message.chat.id
    chat_data[chat_id] = user
    user.push_stage('resume_stage')
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()))
    user.print_stage()
    bot.send_message(chat_id, hs.msg_creator(database.read(user.get_user_id())))
    cancel(message)

'''
@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                      message.text, 'settings_stage', chat_data[message.chat.id]['language']))
def settings(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('settings_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'language_choose_stage', chat_data[message.chat.id]['language']))
def language_choose(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('language_choose_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'language_change_stage', chat_data[message.chat.id]['language']))
def language_change(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('language_change_stage')
    print(chat_data[chat_id]['stage'])
    chat_data[chat_id]['language'] = hs.language_change(message.text)
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']))
    cancel(message)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                          message.text, 'make_note_stage', chat_data[message.chat.id]['language']))
def make_note(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('make_note_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'shift_stage', chat_data[message.chat.id]['language']))
def shift(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('shift_stage')
    chat_data[chat_id]['source'] = message.text
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'source_stage', chat_data[message.chat.id]['language']))
def source(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('source_stage')
    chat_data[chat_id]['shift'] = message.text
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                           message.text, 'message_counter_stage', chat_data[message.chat.id]['language']))
def message_counter(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('message_counter_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language'])
    print(chat_data[chat_id]['stage'])
    chat_data[chat_id]['message_counter'] = message.text
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']), reply_markup=markup)

    res = (f'user: {message.chat.username}, source: {chat_data[chat_id]['source']}, '
           f'shift: {chat_data[chat_id]['shift']}, messages: {chat_data[chat_id]['message_counter']}')
    bot.send_message(chat_id, res)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                           message.text, 'approve_stage', chat_data[message.chat.id]['language']))
def approve(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('approve_stage')
    print(chat_data[chat_id]['stage'])
    database.insert(chat_data[chat_id])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top(), chat_data[chat_id]['language']))
    return menu(message)
'''
@bot.message_handler()
def trash(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Ошибка ввода')

bot.infinity_polling()

#DONE Добавить утро, день, вечер и ночь после выбора источника
#TODO Добавить больше 10 сообщений
#TODO Добавить счетчик смен
#TODO Подумать над названиями кнопок и добавить эмодзи
#TODO Добавить аватарку и описание
#DONE Переписать движение по меню на СТЕК
#DONE Сделать клавиши в ряд а не списком
#DONE Закинуть бота на клауд
#DONE Переписать кнопки на словарь словарей (user_buttons и service buttons)
#TODO Форматирование сообщения вот в таком виде
#TODO Настроить форматирование для вывода
#TODO Выделить жирным дата, источник, время суток
'''
Дата: 11/03/26 (утро/день/вечер/ночь)
Количество вопросов: 10
Источник: amo 
Количество вопросов: к
Источник: беседа
'''

#TODO Переписать юзера на класс
#TODO Реализовать редактирование записей
#TODO Написать доку для пользователей
#DONE Добавить вкладку настроек
#DONE Добавить поддержку нескольких языков