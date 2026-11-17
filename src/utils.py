from telebot import types
from src.managers import storage
import pendulum

def button_creator(user_stage, user_lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    layout = storage.get_buttons_names(user_stage, user_lang)
    buttons = [button for button in layout]
    return markup.add(*buttons)

def message_writer(user_stage, user_lang):
    res = storage.get_message(user_stage, user_lang)
    #print(res)
    if res is None:
        return ''
    return res

def save_get(chat_data, user_id, func):
    try:
        return func(chat_data.get(user_id))
    except:
        return None

#TODO Переписать три функции в одну, так как они повторяют друг друга
def stage_manager(user_stage, user_input, handler_stage, user_lang):
    try:
        user_button_id = storage.get_button_id(user_input, user_lang)
        next_user_stage = storage.get_transition_stage(user_stage, user_button_id)
    except:
        return False
    if (next_user_stage == handler_stage) and (next_user_stage is not None):
        return True
    return False

def back_manager(user_stage, user_input, user_lang):
    try:
        stage_buttons = storage.get_buttons_ids(user_stage)
        user_button_id = storage.get_button_id(user_input, user_lang)
    except:
        return False
    if user_button_id == 'back' and  user_button_id  in stage_buttons:
        return True
    return False

def cancel_manager(user_stage, user_input, user_lang):
    try:
        stage_buttons = storage.get_buttons_ids(user_stage)
        user_button_id = storage.get_button_id(user_input, user_lang)
    except:
        return False
    if user_button_id == 'from_scratch' and  user_button_id  in stage_buttons:
        return True
    return False

def language_change(user_input, user_lang):
    user_button_id = storage.get_button_id(user_input, user_lang)
    if user_button_id == 'eng_button':
        return 'eng'
    else:
        return 'ru'

def data_transformer(data):
    res = []
    counter = 1
    for e in data[::-1]:
        date = pendulum.parse(e[0], tz='Europe/Paris').format('DD/MM/YYYY')
        day = pendulum.parse(e[0], tz='Europe/Paris').format('dddd')
        res.append((counter, date, day, e[1], e[2], e[3]))
        counter += 1
    return res