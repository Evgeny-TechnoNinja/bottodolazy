bot_name = 'Лени Бот'

sticker_path = {
    'hello': 'static/images/lazyhello.webp',
    'returned': 'static/images/lazyreturned.webp',
    'main': 'static/images/lazymainmenu.webp'
}

dialogue = {
    'welcome_text': 'Привет! Дорогой друг {}.\n'
                    'Я {}. Твой помощник по делам на ближайшее время.',
    'user_returned': 'С возвращением, {}.\n '
                     '{} задач: <b>{}</b>\n '
                     '{} задач: <b>{}</b>\n',
    'more_info': '{}, хотите узнать подробней?',
    'change_list': 'Выберете список:',
    'task_desc': 'Опишите задачу:',
    'add_success': 'Задача добавлена в список',
    'not_success': 'Что-то пошло не так. Ошибка!',
    'main_menu': 'Главное меню',
}

menu_main_items = {
    'add': '\U0000270D Добавить',
    'view': '\U0001F4D6 Просмотр',
    'edit': '\U0001F4DD Редактировать',
    'notifi': '\U0001F4E3 Уведомления',
    'help': '\U00002753 Помощь',
}

inline_btn = {
    'help': {
        'more_help_info': 'Хочу...',
    },
}

menu_list_items = {
    'important': '\U0001F4D5 Важный',
    'ordinary': '\U0001F4D7 Обычный',
    'back': '\U00002B05 Назад',
}

pic_task_status = {
    'ready': '\U00002705',
    'not_ready': '\U000025FB'
}

help_todo = {
    'short_info': f'<b>{menu_main_items["add"]}</b> - <i>Добавить задачи</i>\n'
                  f'<b>{menu_main_items["view"]}</b> - <i>Просмотр задач</i>\n'
                  f'<b>{menu_main_items["edit"]}</b> - <i>Править задачи</i>\n'
                  f'<b>{menu_main_items["notifi"]}</b> - <i>Задать интервал</i>\n'
                  f'<b>{menu_main_items["help"]}</b> - <i>Посмотреть помощь</i>\n',
    'full_info': 'Этот бот поможет вам вести список дел.\n'
                 f'Чтобы начать работать со списком, нажмите кнопку \"<b>{menu_main_items["add"]}</b>\". '
                 'Выберите нужный список и напишите в него задачу.\n'
                 '\n'
                 'Для задач есть два разных списка:\n'
                 f'\"<b>{menu_list_items["ordinary"]}</b>\" - для второстепенных задач.\n'
                 f'\"<b>{menu_list_items["important"]}</b>\" - для самых важных задач, его основное отличие от '
                 'обычного списка - это уведомления. Как это работает? '
                 f'Через время вам от {bot_name + "а"} придёт напоминание'
                 ' о какой-либо невыполненной задаче из важного списка.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["notifi"]}</b>\" позволяет настроить временной интервал напоминания'
                 ' или отключить его. По умолчанию напоминания работают через каждый час.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["view"]}</b>\" покажет все ваши записи в списках.\n'
                 '\n'
                 f'Кнопка \"<b>{menu_main_items["edit"]}</b>\" даст доступ к возможностям изменять текст задач, '
                 'отметить их как "готовые" или удалять задачи.\n'
}

table_asset = {
    'separator': '<pre>-----------------------------</pre>',
    'task_start_desc': '<b>{list_item}:</b>\n{separator}\n',
    'task_desc': '{status} <b>{task}</b>\n{separator}\n',
    'task_empty': '<em>Список задач пуст</em>'
}

