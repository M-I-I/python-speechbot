"""
Простой telegram бот с инлайн кнопками, в котором заложено краткое описание синтаксиса языка программирования Python.
Также бот отвечает на текстовые сообщения в telegram, отправляя в ответ введённый пользователем текст в формате Voice(голосовое сообщение).
"""


# Импортируем нужные библиотеки и модули.
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from voice import text_to_file
from theory import theory_dict


# Получаем токен от BotFather в telegram и записываем его в переменную "TOKEN".
TOKEN = "Вставьте сюда ваш токен"


# Создаём переменные с уникальными идентификаторами для кнопок инлайн клавиатур.
# Идентификатор("callback_data") это то, что будет присылать telegram при нажатии на каждую кнопку.
CALLBACK_BUTTON1_YES = "callback_button1_yes"
CALLBACK_BUTTON2_NO = "callback_button2_no"
CALLBACK_BUTTON3_GENERAL = "callback_button3_general"
CALLBACK_BUTTON4_TYPES = "callback_button4_types"
CALLBACK_BUTTON5_SYNTAX_1 = "callback_button5_syntax_1"
CALLBACK_BUTTON5_SYNTAX_2 = "callback_button5_syntax_2"
CALLBACK_BUTTON5_SYNTAX_3 = "callback_button5_syntax_3"
CALLBACK_BUTTON5_SYNTAX_4 = "callback_button5_syntax_4"
CALLBACK_BUTTON6_MORE = "callback_button6_more"
CALLBACK_BUTTON7_BACK = "callback_button7_back"
CALLBACK_BUTTON8_ZEN = "callback_button8_zen"
CALLBACK_BUTTON9_WEBSITE = "callback_button9_website"


# Создаём словарь с названиями кнопок.
TITLES = {
    CALLBACK_BUTTON1_YES: "Да, давай! 🤓👍",
    CALLBACK_BUTTON2_NO: "Нет, давай в другой раз 😞",
    CALLBACK_BUTTON3_GENERAL: "Общая информация 📖",
    CALLBACK_BUTTON4_TYPES: "Типы и структуры данных 📙",
    CALLBACK_BUTTON5_SYNTAX_1: "Выполнение кода Python 📘",
    CALLBACK_BUTTON5_SYNTAX_2: "Отступы в Python  📗",
    CALLBACK_BUTTON5_SYNTAX_3: "Комментарии 📕",
    CALLBACK_BUTTON5_SYNTAX_4: "Строки документации 📒",
    CALLBACK_BUTTON6_MORE: "Ещё ➡️",
    CALLBACK_BUTTON7_BACK: "Назад ⬅️",
    CALLBACK_BUTTON8_ZEN: "Посмотреть Дзен Пайтона 🧙‍♂️",
    CALLBACK_BUTTON9_WEBSITE: "Перейти на официальный сайт Python 🌐"
}


def keyboard_start():
    """
    Получить клавиатуру для начального сообщения.
    """
    # Клавиатура состоит из списка содержащего вложенные списки.
    # Каждый вложенный список внутри списка "keyboard" - это один горизонтальный ряд кнопок. Каждый элемент внутри вложенного списка - кнопка клавиатуры.
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_YES], callback_data=CALLBACK_BUTTON1_YES),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_NO], callback_data=CALLBACK_BUTTON2_NO)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_1():
    """
    Получить клавиатуру основного меню с темами по python.
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_GENERAL], callback_data=CALLBACK_BUTTON3_GENERAL)
        ], 
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_TYPES], callback_data=CALLBACK_BUTTON4_TYPES)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_SYNTAX_1], callback_data=CALLBACK_BUTTON5_SYNTAX_1)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_SYNTAX_2], callback_data=CALLBACK_BUTTON5_SYNTAX_2)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_SYNTAX_3], callback_data=CALLBACK_BUTTON5_SYNTAX_3)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_SYNTAX_4], callback_data=CALLBACK_BUTTON5_SYNTAX_4)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_MORE], callback_data=CALLBACK_BUTTON6_MORE)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_2():
    """
    Получить дополнительную клавиатуру с действиями.
    Возможно получить только при нажатии кнопки на основной клавиатуре.
    """
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_ZEN], callback_data=CALLBACK_BUTTON8_ZEN)
        ],
        # Данная кнопка ниже не отправляет пользователю никакого сообщения, а предлагает перейти на официальный сайт Python.
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_WEBSITE], callback_data=CALLBACK_BUTTON9_WEBSITE, url="https://www.python.org/")
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_BACK], callback_data=CALLBACK_BUTTON7_BACK)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback_handler(update: Update, context: CallbackContext):
    """
    Обработчик ВСЕХ кнопок со ВСЕХ клавиатур.
    """

    query = update.callback_query
    data = query.data
    
    keyboard_1_text = "\n\nВыберите тему:"
    keyboard_2_text = "\n\nВыберите один из вариантов:"

    # При нажатии на кнопку telegram отправляет ответ в виде callback_data.
    # В зависимости от значения callback_data подбирается нужная теория из словаря "theory_dict",
    # отправляется ответным сообщением пользователю, прикрепляется нужная клавиатура.
    if data == CALLBACK_BUTTON1_YES:
        query.edit_message_text(
            text=theory_dict["HISTORY"] + keyboard_1_text,
            reply_markup=keyboard_1()
        )   
    elif data == CALLBACK_BUTTON2_NO:
        query.edit_message_text(
            text="Ок, если передумаете - приходите! Вы знаете, где меня найти 😉😎"
        )
    elif data == CALLBACK_BUTTON3_GENERAL:
        query.edit_message_text(
            text=theory_dict["GENERAL"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON4_TYPES:
        query.edit_message_text(
            text=theory_dict["TYPES"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON5_SYNTAX_1:
        query.edit_message_text(
            text=theory_dict["SYNTAX_1"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON5_SYNTAX_2:
        query.edit_message_text(
            text=theory_dict["SYNTAX_2"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON5_SYNTAX_3:
        query.edit_message_text(
            text=theory_dict["SYNTAX_3"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON5_SYNTAX_4:
        query.edit_message_text(
            text=theory_dict["SYNTAX_4"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON6_MORE:
        query.edit_message_text(
            text=theory_dict["KEYBOARD_2"] + keyboard_2_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_2()
        )
    elif data == CALLBACK_BUTTON7_BACK:
        query.edit_message_text(
            text=theory_dict["HISTORY"] + keyboard_1_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_1()
        )
    elif data == CALLBACK_BUTTON8_ZEN:
        query.edit_message_text(
            text=theory_dict["ZEN"] + keyboard_2_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard_2()
        )


def start(update: Update, context: CallbackContext):
    """
    Команда запуска бота и получения приветственного сообщения.
    """
    update.message.reply_text(
        text=f"Привет, {update.effective_user.first_name}!"
    )
    update.message.reply_text(
        text="Я бот - Питончик)\nУ меня для вас есть небольшая вводная теория по увлекательному языку программирования - Python!"
    )
    file_name_1 = text_to_file(
        text="Кстати, язык программирования python научил меня разговаривать!"
    )
    update.message.reply_voice(
        voice=open(file_name_1, "rb")
    )
    update.message.reply_text(
        text="Хотите узнать про Python?)",
        reply_markup=keyboard_start()
    )
    

def help_handler(update: Update, context: CallbackContext):
    """
    Команда получения помощи.
    """
    help_text = "Это небольшой бот с интерактивными кнопками и общей информацией о языке программирования Python.\n\nВы можете получить краткую теорию нажав на кнопку с соответствующим разделом.\n\nТакже бот умеет преобразовывать отправленное вами текстовое сообщение в голосовое. Просто отправьте любой текст боту и он вернет вам его в формате голосового сообщения."
    update.message.reply_text(help_text)


def reply(update: Update, context: CallbackContext):
    """
    Команда преобразования входящего текстового сообщения в голосовое с помощью модуля voice.py
    """
    file_name_2 = text_to_file(
        update.message.text
    )
    update.message.reply_voice(
        voice=open(
            file_name_2, "rb"
        )
    )


updater = Updater(TOKEN)


# Создаём обработчики команд.
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("help", help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
updater.dispatcher.add_handler(CallbackQueryHandler(callback=keyboard_callback_handler))


# Начинаем бесконечную обработку входящих сообщений
updater.start_polling()
updater.idle()
