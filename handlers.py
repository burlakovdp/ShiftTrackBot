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

def button_creator(user_stage, language):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    layout = language_translater(b.stage,'buttons', user_stage, language)
    items = [types.KeyboardButton(button) for button in layout]
    return markup.add(*items)

#TODO Переписать три функции в одну, так как они повторяют друг друга
def stage_manager(user_stage, user_input, handler_stage, user_lang):
    user_button = None

    for button in b.buttons[user_lang]:
        if b.buttons[user_lang][button] == user_input:
            user_button = button
    try:
        next_user_stage = None
        if user_button in b.stage[user_stage]['transition']:
            next_user_stage = b.stage[user_stage]['transition'][user_button]
    except:
        return False
    if (next_user_stage == handler_stage) and (next_user_stage is not None):
        return True
    return False

def back_manager(user_stage_stack, user_input, user_lang):
    user_button = None
    for button in b.buttons[user_lang]:
        if b.buttons[user_lang][button] == user_input:
            user_button = button

    if not user_button == 'back':
        return False

    if user_stage_stack.size() > 1:
       return True

    return False

def cancel_manager(user_stage, user_input, user_lang):
    user_button = None
    for button in b.buttons[user_lang]:
        if b.buttons[user_lang][button] == user_input:
            user_button = button
    if not user_button == 'from_scratch':
        return False
    print(user_input)
    if not user_input in language_translater(b.stage, 'buttons', user_stage, user_lang):
        return False
    return True

def message_writer(user_stage, user_lang):
    res = language_translater(b.stage, 'message', user_stage, user_lang)
    print(res)
    if res is None:
        return ''
    return res

def language_change(lang):
    if lang == 'Русский':
        return 'ru'
    elif lang == 'English':
        return 'eng'
    return 'ru'

#TODO нужен вот такой вид на return [BUTTONS['make_note'], BUTTONS['resume'], BUTTONS['settings']]// MESSAGE['resume_stage']
def language_translater(data_stage, data_type, user_stage, user_lang):
    if data_type == 'buttons':
        type_storage = b.buttons
    elif data_type == 'message':
        type_storage = b.message
    else:
        return False

    buttons = data_stage[user_stage][data_type]

    res = []
    for elem in type_storage[user_lang]:
        if elem in buttons:
            res.append(type_storage[user_lang][elem])
    return res


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