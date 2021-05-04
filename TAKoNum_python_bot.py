import telebot
from telebot import types
from integrate import shared_property, trapezoid, simpson

api_token = '1729042010:AAEzMUnDxm1WI--y410-H0fNiYu-FNmA3oQ'
bot = telebot.TeleBot(api_token)

error_bound_msg = "Unable to continue the operation, because lower bound is greater than upperbound, to restart the progress, type /calculate again"
n_value_msg = "Unable to continue the operation, because n segment less than 2, to restart the progress, type /calculate again"

@bot.message_handler(commands=['exit'])
def send_help(message):
    print('bot has been shutdown')
    bot.reply_to(message, 'See you')
    bot.polling(none_stop=True)

@bot.message_handler(commands=['calculate'])
def start(message):
    bot.send_message(message.chat.id, "Type the expression")
    shared_property.func = message.text
    bot.register_next_step_handler(message, choice_handler)

def choice_handler(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Trapezoid', 'Simpson')
    bot.reply_to(message, "Select computation method" ,reply_markup=markup)
    bot.register_next_step_handler(message, reply_handler)

def reply_handler(message):
    if(message.text == "Trapezoid"):
        msg = bot.reply_to(message, "Specify number of trapezoid")
        trapezoid.n = message.text
        bot.register_next_step_handler(msg, trapezoid_a_handler)
    elif(message.text == "Simpson"):
        msg = bot.reply_to(message, "Specify number of segment")
        simpson.n = message.text
        bot.register_next_step_handler(msg, simpson_b_handler)

#running trapezoid handler
def trapezoid_a_handler(message):
    bot.reply_to(message, "Specify lower bound value (a)")
    trapezoid.a = message.text
    bot.register_next_step_handler(message, trapezoid_b_handler)

def trapezoid_b_handler(message):
    bot.reply_to(message, "Specify upper bound value (b)")
    trapezoid.b = message.text
    bot.register_next_step_handler(message, trapezoid_check_bound_handler)

def trapezoid_check_bound_handler(message):
    if(trapezoid.a > trapezoid.b):
        bot.send_message(message.chat.id, error_bound_msg)

#running simpson handler
def simpson_a_handler(message):
    bot.reply_to(message, "Specify lower bound value (a)")
    simpson.a =  message.text
    bot.register_next_step_handler(message, simpson_b_handler)

def simpson_b_handler(message):
    bot.reply_to(message, "Specify upper bound value (b)")
    simpson.b = message.text
    bot.register_next_step_handler(message, simpson_check_bound_handler)

def simpson_check_bound_handler(message):
    if(simpson.n < 2):
        bot.send_message(message.chat.id, n_value_msg)
    elif(simpson.a > simpson.b):
        bot.send_message(message.chat.id, error_bound_msg)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=0.5)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

print('bot start running')
bot.polling(none_stop=False)