import telebot
from telebot import types

TOKEN = '419956455:AAGvt0ESW5g7WmHTT9av557_Tm13rjmXCnM'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(m):
    """Отвечаем на команду /start
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['СДЕЛАТЬ КРУТЫЕ БРЭЙДЫ']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['СФОТАТЬСЯ В ЗЕЛЕНОМ АВТОБУСЕ']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['ПОЛУЧИТЬ СЕКРЕТНУЮ СКИДКУ']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['СОХРАНИТЬ МОДНЫЙ СТИКЕРПАК']])
    keyboard.row(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['СТАТЬ АМБАССАДОРОМ']])
    bot.send_message(m.chat.id, "Привет, я чат-бот MATRIX, который будет сегодня жужжать пчелой для всех гостей ПИКНИКА АФИШИ! Давай расскажу, что мы приготовили для тебя сегодня:", reply_markup=keyboard)

@bot.callback_query_handler(func= lambda c: True)
def inline(c):
    if c.data == 'СДЕЛАТЬ КРУТЫЕ БРЭЙДЫ':
        bot.send_message(chat_id=c.message.chat.id, text="Какой фестиваль можно представить без кос? Команда стилистов MATRIX целый день будет плести яркие брэйды с канекалоном всем желающим абсолютно бесплатно! Для того чтобы записаться, подойди на стойку ресепшн в бьюти-баре MATRIX. Торопись, желающих очень много!")
    elif c.data == 'СФОТАТЬСЯ В ЗЕЛЕНОМ АВТОБУСЕ':
        bot.send_message(chat_id=c.message.chat.id, text="В нашем зеленом фотобасе можно сделать крутые фото, которые сразу можно отправить себе на почту или распечатать прямо на месте. А если выложить фото в соцсети с #liveRAW и показать нашему промоутеру, то можно получить набор крутых наклеек BIOLAGE RAW. Торопись, количество наклеек ограничено")
    elif c.data == 'ПОЛУЧИТЬ СЕКРЕТНУЮ СКИДКУ':
        bot.send_message(chat_id=c.message.chat.id, text="Крутые продукты профессионального ухода за волосами MATRIX со скидкой 30% на www.matrix.ru. До конца лета для всех гостей ПИКНИКА по кодовому слову PICNICMATRIX. Ура!")
    elif c.data == 'СОХРАНИТЬ МОДНЫЙ СТИКЕРПАК':
        bot.send_message(chat_id=c.message.chat.id, text="Лови набор стикеров!")
    elif c.data == 'СТАТЬ АМБАССАДОРОМ':
        bot.send_message(chat_id=c.message.chat.id, text="Этой осенью запустится профессиональная эко-гамма по уходу за волосами Biolage RAW. Это не просто продукты, это манифест иного образа жизни. Хочешь узнать первым и стать лидером мнений новой гаммы? Оставляй свой e-mail, и мы отправим тебе инструкцию. #liveRAW")

bot.polling()
