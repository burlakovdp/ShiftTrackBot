import telebot
from telebot import types
from config import TOKEN

import utils as u
from managers import UserManager
import database

API_TOKEN = TOKEN
DEFAULT_LANGUAGE = 'eng'
bot = telebot.TeleBot(API_TOKEN)

chat_data = {}

@bot.message_handler(commands=['start'])
def menu_stage(message):
    chat_id = message.chat.id
    user = UserManager()
    chat_data[chat_id] = user
    user.add_user_id(message.from_user.id)
    user.push_stage('menu_stage')

    #TODO Ask professor
    user_language = database.read_user_language(user.get_user_id())
    if user_language is None:
        user_language = DEFAULT_LANGUAGE

    user.add_data('language', user_language)
    #user.print_stage()
    markup = u.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, u.message_writer(user.get_stage(),
                                                user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.back_manager(chat_data[message.chat.id].get_stage(),
                                                          message.text, chat_data[message.chat.id].get_language()))
def back(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.pop_stage()
    markup = u.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.cancel_manager(chat_data[message.chat.id].get_stage(),
                                                            message.text, chat_data[message.chat.id].get_language()))
def cancel(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    while user.get_size_stage() > 1:
        user.pop_stage()
    markup = u.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'resume_stage',
                                                           chat_data[message.chat.id].get_language()))
def resume_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('resume_stage')
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()))
    #user.print_stage()
    bot.send_message(chat_id, u.msg_creator(database.read(user.get_user_id())))
    cancel(message)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                      message.text, 'settings_stage',
                                                           chat_data[message.chat.id].get_language()))
def settings_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('settings_stage')
    markup = u.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'language_choose_stage',
                                                           chat_data[message.chat.id].get_language()))
def language_choose_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('language_choose_stage')
    markup = u.button_creator(user.get_stage(), user.get_language())
    #user.print_stage()
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'language_change_stage',
                                                           chat_data[message.chat.id].get_language()))
def language_change_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('language_change_stage')
    #user.print_stage()
    language = u.language_change(message.text, user.get_language())
    user.add_data('language', language)
    database.update_user_language(user.get_user_id(), language)
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()))
    cancel(message)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                          message.text, 'shift_stage',
                                                           chat_data[message.chat.id].get_language()))
def shift_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('shift_stage')
    markup = u.button_creator(user.get_stage(), user.get_language())
    #user.print_stage()
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)

@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'counter_stage_1',
                                                           chat_data[message.chat.id].get_language()))
def counter_stage_1(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('counter_stage_1')
    user.add_data('shift', message.text)
    markup = u.button_creator(user.get_stage(), user.get_language())
    #user.print_stage()
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'counter_stage_2',
                                                           chat_data[message.chat.id].get_language()))
def counter_stage_2(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('counter_stage_2')
    user.add_data('counter_stage_1', message.text)
    markup = u.button_creator(user.get_stage(), user.get_language())
    #user.print_stage()
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'check_stage',
                                                           chat_data[message.chat.id].get_language()))
def check_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('check_stage')
    user.add_data('counter_stage_2', message.text)
    markup = u.button_creator(user.get_stage(), user.get_language())
    #user.print_stage()
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)

    res = (f'user: {message.chat.username}, shift: {user.get_data('shift')}, '
           f'amo: {user.get_data('counter_stage_1')}, tg: {user.get_data('counter_stage_2')}')
    bot.send_message(chat_id, res)


@bot.message_handler(func=lambda message: u.stage_manager(chat_data[message.chat.id].get_stage(),
                                                           message.text, 'approve_stage',
                                                           chat_data[message.chat.id].get_language()))
def approve_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('approve_stage')
    #user.print_stage()
    database.insert_data(user.get_user_id(), user.get_data('shift'),
                         user.get_data('counter_stage_1'), user.get_data('counter_stage_2'))
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()))
    return menu_stage(message)

@bot.message_handler(func=lambda message: True)
def wrong_input_stage(message):
    chat_id = message.chat.id
    user = chat_data[chat_id]
    user.push_stage('wrong_input_stage')
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()))
    user.pop_stage()
    markup = u.button_creator(user.get_stage(), user.get_language())
    bot.send_message(chat_id, u.message_writer(user.get_stage(), user.get_language()), reply_markup=markup)

bot.infinity_polling()