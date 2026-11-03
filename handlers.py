import telebot
from telebot import types

from prettytable import PrettyTable

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
        return (type(int(text)) is int) and int(text) > 0
    except ValueError:
        return False

def info_printer(data):
    res = PrettyTable()
    res.field_names= ['Источник', 'Количество сообщений', 'Дата']
    for t in data:
        res.add_row([t[0], t[1], t[2]])
    return res
