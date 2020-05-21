import telebot
from telebot import types

token = "1299839204:AAH2TlkxdjhQUyEh1fKIjZg6AaZYN2grRIU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_start(message) :
   user_markup = telebot. types. ReplyKeyboardMarkup (True , False)
   user_markup.row('/start')
   bot.send_message(message.from_user.id, 'Напиши любое сообщение, чтобы начать работу', reply_markup=user_markup)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    bot.send_message(message.chat.id, "Сейчас появится кнопка")
    markup = types.InlineKeyboardMarkup(row_width=2)


    directory = "C:\Users\Home\Desktop\japan"
    img1 = open(directory + "dbBn-ZxvTe0.jpg", "rb")
    bot.send_photo(message.from_user.id, img1, "Хонсю (яп. 本州 хонсю:) Самый большой и самый важный остров  Японии — остров Хонсю."
                                               "На это острове проживает 98 миллионов человек. Население Японии составляет 128 миллионов человек, поэтому большинство из них живут в Хонсю."                            
                                               "Метрополия Токио с населением 38 миллионов человек также находится на этом острове."
      
      
      
    item1 = types.InlineKeyboardButton("Достопримечательность 1", callback_data="bot1")
    item2 = types.InlineKeyboardButton("Остров 2", callback_data="bot1")
    item3 = types.InlineKeyboardButton("Остров 3", callback_data="bot1")
    item4 = types.InlineKeyboardButton("Остров 4", callback_data="bot1")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выбираем остров', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "bot1":
                bot.send_message(call.message.chat.id, "Первый остров")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Поехали!")
                item2 = types.KeyboardButton("Назад")
                markup.add(item1, item2)
                bot.send_message(call.message.chat.id, "Отправляемся?", reply_markup=markup)
    except Exception as e:
        print(repr(e))

bot.polling (none_stop=True)
