from stack import Stack

class StorageManager:
    def __init__(self):
        self.buttons = {
            'eng': {
                'make_note': '📝 Add note',
                'resume': '📊 Summary',
                'amo': 'Amo',
                'tg': 'Telegram',
                'approve': '✅ Yes',
                'back': '🔙 Back',
                'from_scratch': '🏠 Main menu',
                'digits': ['0','1','2','3','4','5', '6', '7', '8', '9',
                           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                'settings': '⚙️ Settings',
                'lang_change': '🌐 Change language',
                'rus_button': '🇷🇺 Русский',
                'eng_button': '🇬🇧 English',
                'morning': 'Morning',
                'day': 'Day',
                'evening': 'Evening',
                'night': 'Night'
            },
            'ru' : {
                'make_note': '📝 Сделать запись',
                'resume': '📊 Сводка',
                'amo': 'Амо',
                'tg': 'Чат в телеграме',
                'approve': '✅ Да',
                'back': '🔙 Назад',
                'from_scratch': '🏠 Вернуться в начало',
                'digits': ['0','1','2','3','4','5', '6', '7', '8', '9',
                           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                'settings': '⚙️ Настройки',
                'lang_change': '🌐 Смена языка',
                'rus_button': '🇷🇺 Русский',
                'eng_button': '🇬🇧 English',
                'morning': 'Утро',
                'day': 'День',
                'evening': 'Вечер',
                'night': 'Ночь'
            }
        }
        self.message = {
            'eng': {
                'menu_stage': '🧭 What would you like to do?',
                'resume_stage': '📊 Here is your summary:',
                'shift_stage': '🕒 Choose your shift:',
                'counter_stage_1': '💬 How many messages did you handle in Amo?',
                'counter_stage_2': '✈️ And how many in Telegram chat?',
                'check_stage': '👀 Let’s double-check — does everything look right?',
                'approve_stage': '🎉 Awesome! Your data has been saved.',
                'settings_stage': '⚙️ Here are your settings:',
                'language_choose_stage': '🌐 Which language do you prefer?',
                'language_change_stage': '✅ Done! Language updated.',
                'wrong_input_stage': '🤔 Hmm, I didn’t quite get that. Could you try entering it again?',
                'wrong_input_stage_no_start': "Looks like we haven't started yet! Type /start to begin."
            },
            'ru': {
                'menu_stage': '🧭 Выбери нужное действие:',
                'resume_stage': '📊 Вот твоя сводка:',
                'shift_stage': '🕒 Укажи смену:',
                'counter_stage_1': '💬 Сколько сообщений было в Amo?',
                'counter_stage_2': '✈️ А сколько сообщений в Telegram-чате?',
                'check_stage': '👀 Давай проверим — всё верно?',
                'approve_stage': '🎉 Супер! Данные успешно сохранены.',
                'settings_stage': '⚙️ Вот твои настройки:',
                'language_choose_stage': '🌐 Какой язык тебе удобнее?',
                'language_change_stage': '✅ Готово! Язык изменён.',
                'wrong_input_stage': '🤔 Хм, кажется, что-то пошло не так. Попробуй ввести ещё раз!',
                'wrong_input_stage_no_start': 'Похоже, мы ещё не начали! Напиши /start, чтобы запустить бота.'
            }
        }
        self.date = {
            'eng': {

            },
            'ru': {

            }
        }
        self.stage = {
            'menu_stage': {
                'buttons': ['make_note', 'resume', 'settings'],
                'transition': {
                    'make_note': 'shift_stage',
                    'resume': 'resume_stage',
                    'settings': 'settings_stage'
                },
                'message': 'menu_stage'
            },
            'resume_stage' : {
                'buttons': None,
                'next_stage': None,
                'message': 'resume_stage'
            },
            'settings_stage': {
                'buttons': ['back', 'lang_change'],
                'transition': {
                    'lang_change': 'language_choose_stage'
                },
                'message': 'settings_stage'
            },
            'language_choose_stage': {
                'buttons': ['rus_button', 'eng_button', 'back'],
                'transition': {
                    'rus_button': 'language_change_stage',
                    'eng_button': 'language_change_stage'
                },
                'message': 'language_choose_stage'
            },
            'language_change_stage':{
                'buttons': None,
                'message': 'language_change_stage'
            },
            'shift_stage': {
                'buttons': ['morning', 'day', 'evening', 'night', 'back', 'from_scratch'],
                'transition' : {
                    'morning': 'counter_stage_1',
                    'day': 'counter_stage_1',
                    'evening': 'counter_stage_1',
                    'night': 'counter_stage_1',
                    'back': 'menu_stage'
                },
                'message': 'shift_stage'
            },
            'counter_stage_1': {
                'buttons':  ['digits', 'back', 'from_scratch'],
                'transition': {
                    'digits': 'counter_stage_2',
                    'back': 'shift_stage',
                },
                'message': 'counter_stage_1'
            },
            'counter_stage_2': {
                'buttons':  ['digits', 'back', 'from_scratch'],
                'transition': {
                    'digits': 'check_stage',
                    'back': 'counter_stage_1'
                },
                'message': 'counter_stage_2'
            },
            'check_stage': {
                'buttons':  ['approve', 'back', 'from_scratch'],
                'transition' : {
                    'approve': 'approve_stage'
                },
                'message': 'check_stage'
            },
            'approve_stage' : {
                'buttons': None,
                'message': 'approve_stage'
            }
        }

    def get_message(self, user_stage, user_lang):
        return self.message[user_lang][user_stage]

    def get_buttons_names(self, user_stage, user_lang):
        stage_buttons_id = self.stage[user_stage]['buttons']
        try:
            res = []
            for id_button in self.buttons[user_lang]:
                if id_button in stage_buttons_id:
                    if type(self.buttons[user_lang][id_button]) == list:
                        res.extend(self.buttons[user_lang][id_button])
                    else:
                        res.append(self.buttons[user_lang][id_button])
            return res
        except:
            return None

    def get_buttons_ids(self, user_stage):
        return self.stage[user_stage]['buttons']

    def get_button_id(self, user_input, user_lang):
        buttons_ids = self.buttons[user_lang]
        res = None
        for button_id in buttons_ids:
            if user_input in self.buttons[user_lang][button_id]:
                res = button_id
        return res

    def get_transition_stage(self, user_stage, user_button_id):
        return self.stage[user_stage]['transition'][user_button_id]


class UserManager:
    default_language = 'eng'

    def __init__(self):
        self.user_id = None
        self.data = {}
        self.stages = Stack()

    def add_user_id(self, id):
        self.user_id = id

    def add_data(self, key, data):
        self.data[key] = data

    def get_data(self, key):
        return self.data[key]

    @staticmethod
    def get_default_language():
        return UserManager.default_language

    def get_language(self):
        try:
            return self.data['language']
        except:
            return self.get_default_language()

    def get_user_id(self):
        try:
            return self.user_id
        except:
            return None

    def push_stage(self, stage):
        self.stages.push(stage)

    def pop_stage(self):
        return self.stages.pop()

    def get_stage(self):
        try:
            return self.stages.top()
        except:
            return None

    def get_size_stage(self):
        return self.stages.size()

    def stage_is_empty(self):
        return self.stage.is_empty()

    def print_stage(self):
        print(self.get_stage())

storage = StorageManager()
