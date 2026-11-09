import telebot
from telebot import types

from datetime import datetime
import buttons as b

class Stack:
    def __init__(self):
        self.storage = []

    def is_empty(self):
        return not self.storage

    def push(self, e):
        self.storage.append(e)

    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.storage[len(self.storage)-1]
        return None

    def size(self):
        return len(self.storage)

    def __str__ (self):
        return str(self.storage)


def data_initialiser(dict, id):
    dict[id] = {}

def button_creator(user_stage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    layout = b.stage[user_stage]['buttons']
    for button in layout:
        item = types.KeyboardButton(button)
        markup.add(item)
    return markup

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
    #print(next_user_stage, handler_stage, user_button)
    #print('ICI')
    return False

def back_manager(user_stage_stack, user_input):
    user_button = None
    for button in b.BUTTONS:
        if b.BUTTONS[button] == user_input:
            user_button = button

    if not user_button == 'back':
        return False

    if user_stage_stack.size() > 1:
       return True

    return False

def cancel_manager(user_stage, user_input):
    user_button = None
    for button in b.BUTTONS:
        if b.BUTTONS[button] == user_input:
            user_button = button

    if not user_button == 'from_scratch':
        return False

    if not user_input in b.stage[user_stage]['buttons']:
        return False

    return True

def message_writer(user_stage):
    res = b.stage[user_stage]['message']
    if res is None:
        return ''
    return res

def language_change(lang):
    if lang == 'rus':
        b.LANGUAGE = 'rus'
    else:
        b.LANGUAGE = 'eng'

def input_checker(text, buttons):
    return (text != 'Назад' and text != 'Отмена') and (text in buttons)

def int_checker(text):
    try:
        return (type(int(text)) is int) and int(text) >= 0
    except ValueError:
        return False

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