import random

import emoji
from telebot import *
import random

gifs={
    1:"https://media.giphy.com/media/FAFo1M7EC4gRZ4HETH/giphy.gif",
    2:"https://media.giphy.com/media/wRmOK4J2261gI/giphy.gif",
    3:"https://media.giphy.com/media/ITMf6qQnqNLFu/giphy.gif",
    4:"https://media.giphy.com/media/ohT97gdpR40vK/giphy.gif",
    5:"https://media.giphy.com/media/4gsjHZMPXdlGo/giphy.gif",
    6:"https://media.giphy.com/media/lds79WZpA3SN2/giphy.gif",
    7:"https://media.giphy.com/media/WiXMlla4ZFR8Q/giphy.gif",
    8:"https://media.giphy.com/media/qQWufo6HvuGtO/giphy.gif",
    9:"https://media.giphy.com/media/oFqlr0QIOIg8zdxrF8/giphy.gif",
    10:"https://media.giphy.com/media/VAzhi9GfotTXy/giphy.gif",
    11:"https://media.giphy.com/media/dsPBfiEEozyXUXShhB/giphy.gif",
    12:"https://media.giphy.com/media/ZtB2l3jHiJsFa/giphy.gif",
    13:"https://media.giphy.com/media/GUx4WVQJLESaI/giphy.gif",
    14:"https://media.giphy.com/media/AFdcYElkoNAUE/giphy.gif",
    15:"https://media.giphy.com/media/cXaeWuJ1oKO4g/giphy.gif",
    16:"https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif",
    17:"https://media.giphy.com/media/PPgZCwZPKrLcw75EG1/giphy.gif"

}

phrases = {
    1:"Здесь очень жарко или это из-за тебя, Алёна?",
    2:"Мне нужна карта и компас, чтобы не заблудиться в твоих голубых глазах.",
    3:"Алёна словно кофе: горячая, крепкая, вкусная, бодрящая и ароматная.",
    4:"По шкале от 1 до 10, ты 100 баллов.",
    5:"Твои родители, наверное, кулинары, раз у них вышла такая великолепная крошка.",
    6:"Ты прекрасная на 60%. К сожалению, остальные 40% тебя скрыты одеждой.",
    7:"Платье на тебе тютелька в тютельку. Мне нравятся твои тютельки.",
    8:"У тебя ангельское личико, но тело грешницы.",
    9:"Алёна, ты так вкусно пахнешь",
    10:"Ты вроде не подлец, но тебе все к лицу",
    11:"У тебя нет недостатков! Есть только спецэффекты и особенности!",
    12:"Какой у тебя хищный взгляд! Голодная?",
    13:"Лично от Миши: Странно, ты не кварк, почему тогда такая прелестная?",
    14:"АлЁна, с таким лицом мини-юбку не носят!",
    15:"Аллах создал тебя, всё остальное создали в Китае…(Кавказский)",
    16:"Алёна — это как горный цветок, который нужно сорвать, а не подобрать сорванный.(Кавказский)",
    17:"Алёна, ты – самый лучший философ.",
    18:"Алёна, тебе к лицу любая прическа!",
    19:"Ну вы только посмотрите на неё! Какая хорошенькая!!",
    20:"У тя сотка шишки за шестьдесят пять — я возьму, пожалуй\n"
    +"Захожу в клуб и директор такой: «О, добро пожаловать!»\n"
    +"Час дня — влил двойку, понимаю, что пиздец рано\n"
    +"Выстрелил долбоёбу в грудь, у него там пиздец рана\n",
    21:"Алёна, Гусев передавал что ты секси… Реально…",
    22:"Никто так не убирал ди-ранги, как ты….",
    23:"Ты – самая трудолюбивая и ответственная!!! Буду ставить тебя в пример своим детям.",
    24:"Алёна, счастья, здоровья,\n"
    +"море удачи и дачу у моря!",
    25:"Ты знаешь ведь о теории Дарвина, все люди происходят от обезьян. Думаю, тебя это не касается",
    26:"О тебе сообщили в ИНТЕРПОЛ, ты украла сердца многих мужчин иностранцев",
    27:"Ты чудная девушка! С твоим озорством неважно где ударение!",
    28:"Если бы ты жила в прошлые века, ты бы точно стала музой известного художника.",
    29:"Если ты откроешь выставку своих фотографий, не забудь выслать приглашение.",
    30:"Люблю читать твои посты. У тебя очень интересный взгляд на мир.",
    31:"Философ, писатель, модель – ты многогранная личность."
}
def init_bot():  # инициализация бота
    print("Bot_init")
    global bot
    '''
    telegram_token = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_token)
    '''
    no=0
    # для локального тестирования
    bot = telebot.TeleBot("5354496390:AAE9eptr5Ieqhe1kMFNasoJQofNJKm2ExQQ")


init_bot()
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💝")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Привет', reply_markup=markup)
no=0
gif=0
@bot.message_handler(content_types=["text"])
def handle_text(msg):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💝")
    markup.add(item1)
    if msg.text.strip()=="💝":
        global no,gif
        no+=1
        gif+=1
        if no==32:
            no=1
        if gif==18:
            gif=1
        bot.send_message(msg.chat.id, phrases.get(no), reply_markup=markup)
        bot.send_video(msg.chat.id, gifs.get(gif), None, 'Text')

bot.polling()

