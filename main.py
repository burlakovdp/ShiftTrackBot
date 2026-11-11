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
    user = chat_data[chat_id]
    user.pop_stage()
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.cancel_manager(chat_data[message.chat.id].get_stage(),
                                                            message.text, chat_data[message.chat.id].get_language()))
def cancel(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    while user.get_size_stage() > 1:
        user.pop_stage()
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'resume_stage',
                                                           chat_data[message.chat.id].get_language()))
def resume(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('resume_stage')
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()))
    user.print_stage()
    bot.send_message(chat_id, hs.msg_creator(database.read(user.get_user_id())))
    cancel(message)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                      message.text, 'settings_stage',
                                                           chat_data[message.chat.id].get_language()))
def settings(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('settings_stage')
    markup = hs.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'language_choose_stage',
                                                           chat_data[message.chat.id].get_language()))
def language_choose(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('language_choose_stage')
    markup = hs.button_creator(user.get_stage(), user.get_language())
    user.print_stage()
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'language_change_stage',
                                                           chat_data[message.chat.id].get_language()))
def language_change(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('language_change_stage')
    user.print_stage()
    user.add_data('language' ,hs.language_change(message.text))
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()))
    cancel(message)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                          message.text, 'make_note_stage',
                                                           chat_data[message.chat.id].get_language()))
def make_note(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('make_note_stage')
    markup = hs.button_creator(user.get_stage(), user.get_language())
    user.print_stage()
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'shift_stage',
                                                           chat_data[message.chat.id].get_language()))
def shift(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('shift_stage')
    user.add_data('source', message.text)
    markup = hs.button_creator(user.get_stage(), user.get_language())
    user.print_stage()
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'source_stage',
                                                           chat_data[message.chat.id].get_language()))
def source(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('source_stage')
    user.add_data('shift', message.text)
    markup = hs.button_creator(user.get_stage(), user.get_language())
    user.print_stage()
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'message_counter_stage',
                                                           chat_data[message.chat.id].get_language()))
def message_counter(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('message_counter_stage')
    user.add_data('message_counter', message.text)
    markup = hs.button_creator(user.get_stage(), user.get_language())
    user.print_stage()
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)

    res = (f'user: {message.chat.username}, source: {user.get_data('source')}, '
           f'shift: {user.get_data('shift')}, messages: {user.get_data('message_counter')}')
    bot.send_message(chat_id, res)


@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'approve_stage',
                                                           chat_data[message.chat.id].get_language()))
def approve(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('approve_stage')
    user.print_stage()
    database.insert(user.get_user_id(), user.get_data('source'), user.get_data('message_counter'))
    bot.send_message(chat_id, hs.message_writer(user.get_stage(), user.get_language()))
    return menu(message)

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

#DONE Переписать юзера на класс
#TODO Реализовать редактирование записей
#TODO Написать доку для пользователей
#DONE Добавить вкладку настроек
#DONE Добавить поддержку нескольких языков