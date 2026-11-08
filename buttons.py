LANGUAGE = None

buttons_rus = {
    'make_note': 'Сделать запись',
    'resume': 'Сводка',
    'amo': 'Амо',
    'tg': 'Телеграм бот',
    'approve': 'Да',
    'back': 'Назад',
    'from_scratch': 'Вернуться в начало',
    'digits': '1'
}

BUTTONS = buttons_rus

stage = {
    'menu_stage': {
        'buttons': [BUTTONS['make_note'], BUTTONS['resume']],
        'transition':{
            'make_note': 'make_note_stage',
            'resume': 'resume_stage'
        },
        'prev_stage': None
    },
    'resume_stage' : {
        'buttons': None,
        'next_stage': None,
        'prev_stage': 'menu_stage'
    },
    'make_note_stage': {
        'buttons':  [BUTTONS['amo'], BUTTONS['tg'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition': {
            'amo': 'source_stage',
            'tg': 'source_stage',
        },
        'prev_stage' : 'menu_stage'
    },
    'source_stage': {
        'buttons':  [BUTTONS['digits'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition': {
            'digits': 'message_counter_stage'
        },
        'prev_stage': 'make_note_stage'
    },
    'message_counter_stage': {
        'buttons':  [BUTTONS['approve'], BUTTONS['back'], BUTTONS['from_scratch']],
        'transition' : {
            'approve': 'approve_stage'
        },
        'prev_stage': 'source_stage'
    },
    'approve_stage' : {
        'buttons': None,
        'next_stage': 'menu_stage',
        'prev_stage': 'message_counter_stage'
    }
}