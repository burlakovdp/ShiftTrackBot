LANGUAGE = None

buttons_rus = {
    'make_note': 'Сделать запись',
    'resume': 'Сводка',
    'amo': 'Амо',
    'tg': 'Телеграм бот',
    'approve': 'Да',
    'back': 'Назад',
    'from_scratch': 'Вернуться в начало',
    'digits': '1',
    'settings': 'Настройки',
    'lang_change': 'Смена языка',
    'rus_button': 'Русский',
    'eng_button': 'English'
}

buttons_eng = {
    'make_note': 'Make note',
    'resume': 'Resume',
    'amo': 'Amo',
    'tg': 'Telegram bot',
    'approve': 'Yes',
    'back': 'Back',
    'from_scratch': 'To start',
    'digits': '1',
    'settings': 'Settings',
    'lang_change': 'Change language',
    'rus_button': 'Русский',
    'eng_button': 'English'
}

message_rus = {
    'menu_stage': 'Выберите действие:',
    'resume_stage': 'Вот сводка:',
    'make_note_stage': 'Выберите источник',
    'source_stage' : 'Укажите количество сообщений',
    'message_counter_stage': 'Все верно?',
    'approve_stage' : 'Данные добавлены',
    'settings_stage': 'Вот настройки:',
    'language_change_stage': 'Выберите язык'
}

BUTTONS = buttons_rus
MESSAGE = message_rus

stage = {
    'menu_stage': {
        'buttons': [BUTTONS['make_note'], BUTTONS['resume'], BUTTONS['settings']],
        'transition':{
            'make_note': 'make_note_stage',
            'resume': 'resume_stage',
            'settings': 'settings_stage'
        },
        'message': MESSAGE['menu_stage']
    },
    'resume_stage' : {
        'buttons': None,
        'next_stage': None,
        'message': MESSAGE['resume_stage']

    },
    'settings_stage': {
        'buttons': [BUTTONS['lang_change'], BUTTONS['back']],
        'next_stage': 'menu_stage',
        'transition': {
          'lang_change': 'language_change_stage'
        },
        'message': MESSAGE['settings_stage']
    },
    'language_change_stage': {
        'buttons': [BUTTONS['rus_button'], BUTTONS['eng_button'],  BUTTONS['back']],
        'transition': None,
        'next_stage': 'menu_stage',
        'message': MESSAGE['language_change_stage']
    },
    'make_note_stage': {
        'buttons':  [BUTTONS['amo'], BUTTONS['tg'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition': {
            'amo': 'source_stage',
            'tg': 'source_stage',
            'back': 'menu_stage',
        },
        'message': MESSAGE['make_note_stage']
    },
    'source_stage': {
        'buttons':  [BUTTONS['digits'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition': {
            'digits': 'message_counter_stage',
            'back': 'menu_stage'
        },
        'message': MESSAGE['source_stage']
    },
    'message_counter_stage': {
        'buttons':  [BUTTONS['approve'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition' : {
            'approve': 'approve_stage'
        },
        'message': MESSAGE['message_counter_stage']
    },
    'approve_stage' : {
        'buttons': None,
        'next_stage': 'menu_stage',
        'message': MESSAGE['approve_stage']
    }
}