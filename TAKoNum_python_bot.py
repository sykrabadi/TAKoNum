import telebot
from telebot import types
api_token = '1729042010:AAEzMUnDxm1WI--y410-H0fNiYu-FNmA3oQ'
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['exit'])
def send_help(message):
    print('bot has been shutdown')
    bot.reply_to(message, 'See you')
    bot.polling(none_stop=True)

@bot.message_handler(commands=['calculate'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Trapezoid', 'Simpson')
    bot.send_message(message.chat.id, "Select computation method" ,reply_markup=markup)
    bot.register_next_step_handler(message, reply_handler)

def reply_handler(message):
    if(message.text == "Trapezoid"):
        msg = bot.reply_to(message, "Specify number of trapezoid")
        bot.register_next_step_handler(msg, trapezoid_a_handler)
    elif(message.text == "Simpson"):
        msg = bot.reply_to(message, "Specify number of segment")
        bot.register_next_step_handler(msg, simpson_b_handler)

#running trapezoid handler
def trapezoid_a_handler(message):
    bot.reply_to(message, "Specify lower bound value (a)")
    bot.register_next_step_handler(message, trapezoid_b_handler)

def trapezoid_b_handler(message):
    bot.reply_to(message, "Specify upper bound value (b)")

#running simpson handler
def simpson_a_handler(message):
    bot.reply_to(message, "Specify lower bound value (a)")
    bot.register_next_step_handler(message, trapezoid_b_handler)

def simpson_b_handler(message):
    bot.reply_to(message, "Specify upper bound value (b)")

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=0.5)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

print('bot start running')
bot.polling(none_stop=False)

