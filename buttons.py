buttons = {
    'eng': {
        'make_note': 'Make a note',
        'resume': 'Summary',
        'amo': 'Amo',
        'tg': 'Telegram chat',
        'approve': 'Yes',
        'back': 'Back',
        'from_scratch': 'Return to start',
        'digits': '1',
        'settings': 'Settings',
        'lang_change': 'Change language',
        'rus_button': 'Русский',
        'eng_button': 'English',
    },
    'ru' : {
        'make_note': 'Сделать запись',
        'resume': 'Сводка',
        'amo': 'Амо',
        'tg': 'Чат в телеграмме',
        'approve': 'Да',
        'back': 'Назад',
        'from_scratch': 'Вернуться в начало',
        'digits': '1',
        'settings': 'Настройки',
        'lang_change': 'Смена языка',
        'rus_button': 'Русский',
        'eng_button': 'English'
    }
}

message = {
    'eng': {
        'menu_stage': 'Select an action:',
        'resume_stage': 'Here is the summary:',
        'make_note_stage': 'Select a source',
        'source_stage': 'Enter the number of messages',
        'message_counter_stage': 'Is everything correct?',
        'approve_stage': 'Data added',
        'settings_stage': 'Here are the settings:',
        'language_choose_stage': 'Select language',
        'language_change_stage': 'Language changed'
    },
    'ru' : {
        'menu_stage': 'Выберите действие:',
        'resume_stage': 'Вот сводка:',
        'make_note_stage': 'Выберите источник',
        'source_stage' : 'Укажите количество сообщений',
        'message_counter_stage': 'Все верно?',
        'approve_stage' : 'Данные добавлены',
        'settings_stage': 'Вот настройки:',
        'language_choose_stage': 'Выберите язык',
        'language_change_stage': 'Язык сменен'
    }
}

stage = {
    'menu_stage': {
        'buttons': ['make_note', 'resume', 'settings'],
        'transition': {
            'make_note': 'make_note_stage',
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
    'make_note_stage': {
        'buttons':  ['amo', 'tg', 'back', 'from_scratch'],
        'transition': {
            'amo': 'source_stage',
            'tg': 'source_stage',
            'back': 'menu_stage',
        },
        'message': 'make_note_stage'
    },
    'source_stage': {
        'buttons':  ['digits', 'back', 'from_scratch'],
        'transition': {
            'digits': 'message_counter_stage',
            'back': 'menu_stage'
        },
        'message': 'source_stage'
    },
    'message_counter_stage': {
        'buttons':  ['approve', 'back', 'from_scratch'],
        'transition' : {
            'approve': 'approve_stage'
        },
        'message': 'message_counter_stage'
    },
    'approve_stage' : {
        'buttons': None,
        'message': 'approve_stage'
    }
}