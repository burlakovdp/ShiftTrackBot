import telebot
from telebot import types

from datetime import datetime
import buttons as b

def data_initialiser(dict, id):
    dict[id] = {}

def button_creator(user_stage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    layout = b.stage[user_stage]['buttons']
    for button in layout:
        item = types.KeyboardButton(button)
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

def stage_manager(user_stage, user_input, handler_stage):
    user_button = None
    for button in b.BUTTONS:
        if b.BUTTONS[button] == user_input:
            user_button = button

    next_user_stage = None
    if user_button in b.stage[user_stage]['transition']:
        next_user_stage = b.stage[user_stage]['transition'][user_button]

    if (next_user_stage == handler_stage) and (next_user_stage is not None):
        return True
    return False

def language_change(lang):
    if lang == 'rus':
        b.LANGUAGE = 'rus'
    else:
        b.LANGUAGE = 'eng'
