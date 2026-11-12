import telebot
from telebot import types

from datetime import datetime
from managers import *

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

def button_creator(user_stage, user_lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    layout = storage.get_buttons_names(user_stage, user_lang)
    buttons = [button for button in layout]
    return markup.add(*buttons)

def message_writer(user_stage, user_lang):
    res = storage.get_message(user_stage, user_lang)
    print(res)
    if res is None:
        return ''
    return res

#TODO Переписать три функции в одну, так как они повторяют друг друга
def stage_manager(user_stage, user_input, handler_stage, user_lang):
    user_button_id = storage.get_button_id(user_input, user_lang)
    try:
        next_user_stage = storage.get_transition_stage(user_stage, user_button_id)
    except:
        return False
    if (next_user_stage == handler_stage) and (next_user_stage is not None):
        return True
    return False

def back_manager(user_stage, user_input, user_lang):
    stage_buttons = storage.get_buttons_ids(user_stage)
    user_button_id = storage.get_button_id(user_input, user_lang)
    if user_button_id == 'back' and  user_button_id  in stage_buttons:
        return True
    return False

def cancel_manager(user_stage, user_input, user_lang):
    stage_buttons = storage.get_buttons_ids(user_stage)
    user_button_id = storage.get_button_id(user_input, user_lang)
    if user_button_id == 'from_scratch' and  user_button_id  in stage_buttons:
        return True
    return False

def language_change(lang):
    if lang == '🇷🇺 Русский':
        return 'ru'
    elif lang == '🇬🇧 English':
        return 'eng'
    return 'ru'

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