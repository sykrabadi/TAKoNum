import telebot
from telebot import types

api_token = '1729042010:AAEzMUnDxm1WI--y410-H0fNiYu-FNmA3oQ'
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'halo apa kabar?')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'ada yang bisa saya bantu?')

@bot.message_handler(commands=['exit'])
def send_help(message):
    print('bot has been shutdown')
    bot.reply_to(message, 'See you')
    bot.polling(none_stop=True)

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.reply_to(message, 'ini adalah teks')

print('bot start running')
bot.polling(none_stop=False)