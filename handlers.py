import telebot
from telebot import types

from datetime import datetime

def data_initialiser(dict, id):
    dict[id] = {}

def button_creator(buttons_names):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for e in buttons_names:
        item = types.KeyboardButton(e)
        markup.add(item)
    return markup

def input_checker(text, buttons):
    return (text != 'Назад' and text != 'Отмена') and (text in buttons)

def int_checker(text):
    try:
        return (type(int(text)) is int) and int(text) >= 0
    except ValueError:
        return False

# TODO Форматирование сообщения вот в таком виде
'''
Дата: 11/03/26 (утро/день/вечер/ночь)
Количество вопросов: 10
Источник: amo 
Количество вопросов: к
Источник: беседа
'''

def date_transformer(date):
    tmp = date.split('-')
    return f'{tmp[1]}/{tmp[2]}/{tmp[0]}'

def msg_creator(data):
    res = []
    for e in data:
        res.append(f'Дата: {date_transformer(e[2])}\n'
                   f'Количество вопросов: {e[1]}\n'
                   f'Источник: {e[0]}\n'
                   f'---')
    return '\n'.join(res)

