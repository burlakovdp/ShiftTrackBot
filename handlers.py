from io import BufferedRWPair

import telebot
from telebot import types

def data_initialiser(dict, id):
    dict[id] = {}

def button_creator(buttons_names):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for e in buttons_names:
        item = types.KeyboardButton(e)
        markup.add(item)
    return markup

def input_checker(text, buttons):
    return text != 'Назад' and (text in buttons)

def int_checker(text):
    try:
        return (type(int(text)) is int) and int(text) > 0
    except:
        return False

        