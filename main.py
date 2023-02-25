import telebot
from telebot import types
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> <u>{message.from_user.last_name}</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

#
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hi':
#         bot.send_message(message.chat.id, 'Hi!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Your id:{message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('image.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you!", parse_mode='html')



@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow, photo is cool!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("My GitHub", url="https://github.com/FootballOnlooker"))
    bot.send_message(message.chat.id, 'Go to GitHub!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Go to GitHub!', reply_markup=markup)


bot.polling(none_stop=True)
