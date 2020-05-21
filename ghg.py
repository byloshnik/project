import telebot
token = "1299839204:AAH2TlkxdjhQUyEh1fKIjZg6AaZYN2grRIU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_start(message) :
   user_markup = telebot. types. ReplyKeyboardMarkup (True , False)
   user_markup.row('/start','/stop')
   bot.send_message(message.from_user.id, 'Привет, я бот, который помможт тебе узнать больше о Японии! напиши  Выбери остров о котром ты хочешь узнать больше.', reply_markup=user_markup)

@bot.message_handler(commands=["stop"])
def handle_start(message):
   bot.send_message(message.from_user.id,
                    'выбери один из 4 островов оторые хочеь посетить',
                    reply_markup=user_markup)

@bot.message_handlers(content_types=['text'])
bot.send_message(message.chat.id, "Сейчас появится кнопка")
markup = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton("кнопка 1", callback_data="bot1")
item2 = types.InlineKeyboardButton("кнопка 2", callback_data="bot2")
markup.add(item1, item2)
bot.send_message(message.chat.id, '"КНОПКА"', reply_markup=markup)
# #@bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#   try:
#      if call.message:
#         if call.data == "выбор":
#             #bot.send_message(call.message.chat.id, "острова")
#             #directory = "/Users/byloshnik/Desktop/python/telegram_bot/Quest/Pictures/"
#             #img4 = open(directory + "gate_keeper2.png", "rb")
#             #bot.send_photo(call.message.chat.id, img4, '"Хонсю."')
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton("Бежим!")
#             markup.add(item1)
#             item2 = types.KeyboardButton("Бежим!")
#             markup.add(item2)
#             item3 = types.KeyboardButton("Бежим!")
#             markup.add(item3)
#             item4 = types.KeyboardButton("Бежим!")
#             markup.add(item4)
#             item5 = types.KeyboardButton("Бежим!")
#             markup.add(item5)
#   except Exception as e:
#             print(repr(e))
   #hide_markup = telebot.types.ReplyKeyboardHide()
   #bot.send_message(message.from_user.id, '..', reply_markup = hide_markup)


   #@bot.message_handlers(content_types=['text'])
   #bot.sen
   #send_chat_action(self, chat_id, action)
   #bot.polli
   #m
   #send
   #location(self.chat
   #id, latitude, repl

bot.polling (none_stop=True)

#upd = bot.get_updates()
# print(upd)
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

#@bot.message_handler(content_types = ["text"])
#def handle_command(message):
   #if message.text == "Привет":
      #bot.send_message(message.chat.id, "Привет, я бот, который помможт тебе узнать больше о Японии! напиши /start и Выбери остров о котром ты хочешь узнать больше.")

   #else:
     #bot.send_message(message.chat.id, "напиши 'Привет',чтобы начать'")
bot.polling(none_stop=True, interval=0)
