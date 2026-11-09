import telebot
from telebot import types
from config import TOKEN
import buttons as b
import handlers as hs
import database

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

chat_data = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def menu(message):
    chat_id = message.chat.id
    hs.data_initialiser(chat_data, chat_id)
    chat_data[chat_id]['stage'] = hs.Stack()
    chat_data[chat_id]['stage'].push('menu_stage')
    print(chat_data[chat_id]['stage'])
    chat_data[chat_id]['user_id'] = message.from_user.id
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.back_manager(chat_data[message.chat.id]['stage'], message.text))
def back(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].pop()
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.cancel_manager(chat_data[message.chat.id]['stage'].top(), message.text))
def cancel(message):
    chat_id = message.chat.id
    while chat_data[chat_id]['stage'].size() > 1:
        chat_data[chat_id]['stage'].pop()
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'resume_stage'))
def resume(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()))
    bot.send_message(chat_id, hs.msg_creator(database.read(chat_data[chat_id]['user_id'])))

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'settings_stage'))
def settings(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('settings_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'language_change_stage'))
def language_change(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('language_change_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                          message.text, 'make_note_stage'))
def make_note(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('make_note_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                                           message.text, 'source_stage'))
def source(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('source_stage')
    chat_data[chat_id]['source'] = message.text
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                           message.text, 'message_counter_stage'))
def message_counter(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('message_counter_stage')
    markup = hs.button_creator(chat_data[chat_id]['stage'].top())
    print(chat_data[chat_id]['stage'])
    chat_data[chat_id]['message_counter'] = message.text
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()), reply_markup=markup)

    res = f'user: {message.chat.username}, source: {chat_data[chat_id]['source']}, messages: {chat_data[chat_id]['message_counter']}'
    bot.send_message(chat_id, res)

@bot.message_handler(func=lambda message: hs.stage_manager(chat_data[message.chat.id]['stage'].top(),
                                           message.text, 'approve_stage'))
def approve(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'].push('approve_stage')
    print(chat_data[chat_id]['stage'])
    database.insert(chat_data[chat_id])
    bot.send_message(chat_id, hs.message_writer(chat_data[chat_id]['stage'].top()))
    return menu(message)

@bot.message_handler()
def trash(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Ошибка ввода')

bot.infinity_polling()

#DONE Переписать движение по меню на СТЕК
#TODO Добавить утро, день, вечер и ночь после выбора источника
#TODO Настроить форматирование для вывода
#TODO Сделать клавиши в ряд а не списком
#TODO Выделить жирным дата, источник, время суток
#DONE Закинуть бота на клауд
#DONE Переписать кнопки на словарь словарей (user_buttons и service buttons)
#TODO Добавить счетчик смен
#TODO Добавить больше 10 сообщений
#TODO Форматирование сообщения вот в таком виде

'''
Дата: 11/03/26 (утро/день/вечер/ночь)
Количество вопросов: 10
Источник: amo 
Количество вопросов: к
Источник: беседа
'''

#TODO Переписать юзера на класс
#TODO Реализовать редактирование записей
#TODO Подумать над названиями кнопок и добавить эмодзи
#TODO Добавить аватарку и описание
#TODO Написать доку для пользователей
#TODO Добавить вкладку настроек
#TODO Добавить поддержку нескольких языков