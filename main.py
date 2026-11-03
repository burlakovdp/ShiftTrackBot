import telebot
from telebot import types
from config import TOKEN

import handlers
from buttons import buttons
import database

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

chat_data = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def menu(message):
    chat_id = message.chat.id
    handlers.data_initialiser(chat_data, chat_id)
    chat_data[chat_id]['stage'] = 0
    chat_data[chat_id]['user_id'] = message.from_user.id
    markup = handlers.button_creator(buttons['menu'])
    print(chat_data)
    bot.send_message(chat_id, 'Выберите действие:', reply_markup=markup)

@bot.message_handler(func=lambda message: chat_data[message.chat.id]['stage'] == 0
                                          and message.text == 'Сделать запись')
def make_note(message):
    chat_id = message.chat.id
    markup = handlers.button_creator(buttons['source'])
    chat_data[chat_id]['stage'] = 1
    bot.send_message(chat_id, 'Выберите источник', reply_markup=markup)

@bot.message_handler(func=lambda message: chat_data[message.chat.id]['stage'] == 1
                                          and (handlers.input_checker(message.text, buttons['source'])))
def source(message):
    chat_id = message.chat.id
    markup = handlers.button_creator(buttons['digits'])
    if message.text != 'Назад':
        chat_data[chat_id]['source'] = message.text
    bot.send_message(chat_id, 'Укажите количество сообщений', reply_markup=markup)
    chat_data[chat_id]['stage'] = 2

@bot.message_handler(func=lambda message: (chat_data[message.chat.id]['stage'] == 2) and
                                          handlers.int_checker(message.text))
def message_counter(message):
    markup = handlers.button_creator(buttons['approve'])
    chat_id = message.chat.id
    chat_data[chat_id]['message_counter'] = message.text
    bot.send_message(chat_id, 'Все верно?', reply_markup=markup)
    res = f'user: {message.chat.username}, source: {chat_data[chat_id]['source']}, messages: {chat_data[chat_id]['message_counter']} '
    bot.send_message(chat_id, res)
    chat_data[chat_id]['stage'] = 3    

@bot.message_handler(func=lambda message: (chat_data[message.chat.id]['stage'] == 3) and message.text == 'Да')
def approve(message):
    chat_id = message.chat.id
    database.insert(chat_data[chat_id])
    bot.send_message(chat_id, 'Данные добавлены')
    chat_data[chat_id]['stage'] = 0
    return menu(message)
    

@bot.message_handler(func=lambda message: message.text=="Сводка")
def info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Вот сводка:')
    bot.send_message(chat_id, handlers.msg_creator(database.read(chat_data[chat_id]['user_id'])))
    print(handlers.msg_creator(database.read(chat_data[chat_id]['user_id'])))
    
@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
    chat_id = message.chat.id
    if chat_data[chat_id]['stage'] == 0:
        return menu(message)
    else:
        chat_data[chat_id]['stage'] -= 1
        if chat_data[chat_id]['stage'] == 1:
            return make_note(message)
        elif chat_data[chat_id]['stage'] == 2:
            return source(message)
        else:
            return menu(message)

@bot.message_handler(func=lambda message: message.text == 'Отмена')
def cancel(message):
    chat_id = message.chat.id
    chat_data[chat_id]['stage'] = 0
    return menu(message)

@bot.message_handler()
def trash(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Ошибка ввода')

bot.infinity_polling()


#TODO Добавить утро, день, вечер и ночь после выбора источника
#TODO Настроить форматирование для вывода
#TODO Сделать клавиши в ряд а не списком
#TODO Выделить жирным дата, источник, время суток
#TODO Закинуть бота на клауд
#TODO Переписать кнопки на словарь словарей (user_buttons и service buttons)

#TODO Переписать юзера на класс
#TODO Реализовать редактирование записей
#TODO Подумать над названиями кнопок и добавить эмодзи
#TODO Добавить аватарку и описание
#TODO Написать доку для пользователей