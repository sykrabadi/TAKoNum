import telebot
from telebot import types
from integrate import shared_property, trapezoid, simpson

api_token = '<api token here>'
bot = telebot.TeleBot(api_token)

error_bound_msg = "Unable to continue the operation, because lower bound is greater than upperbound, to restart the progress, type calculate again"
n_value_msg = "Unable to continue the operation, because n segment less than 2, to restart the progress, type calculate again"

@bot.message_handler(commands=['exit'])
def send_help(message):
    print('bot has been shutdown')
    msg = u"See you next time! \uE41E"
    bot.reply_to(message,  msg)
    bot.polling(none_stop=True)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = u"""
    Hello, welcome to telegram integration bot!

    The commands : 
    \U0001F916 /start       : Start the conversation
    \U0001F916 /trapezoid   : Calculate integration using trapezoid method
    \U0001F916 /simpson     : Calculate integration using simpson method
    \U0001F916 /exit        : End the conversation

    The rules :
    \u2705 Expression should be written in "x"
    \u2705 Number of segments, lower bound, and upper bound should be numbers
    """
    bot.reply_to(message, msg)

@bot.message_handler(commands=['calculate'])
def start(message):
    bot.reply_to(message, "Type the expression")
    bot.register_next_step_handler(message, function_handler)

def function_handler(message):
    bot.reply_to(message, "Retype the expression")
    func = message.text
    shared_property.func = func
    bot.register_next_step_handler(message, reply_handler)

def choice_handler(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('/Trapezoid', '/Simpson')
    msg = bot.reply_to(message, "Select computation method" ,reply_markup=markup)
    bot.send_message(message.chat.id, msg)
    bot.register_next_step_handler(msg, reply_handler)

def reply_handler(message):
    if(message.text == "/Trapezoid"):
        bot.register_next_step_handler(message, trapezoid_n_handler)
    elif(message.text == "/Simpson"):
        bot.register_next_step_handler(message, simpson_n_handler)
    chat_id = message.chat.id

#running trapezoid handler
@bot.message_handler(commands=['trapezoid'])
def start_handler(message):
    msg = bot.reply_to(message, "Specify function")
    bot.register_next_step_handler(msg, trapezoid_function_handler)

def trapezoid_function_handler(message):
    chat_id = message.chat.id
    function = message.text
    shared_property.func = function
    msg = bot.reply_to(message, "Specify number of trapezoid (n)")
    bot.register_next_step_handler(msg, trapezoid_n_handler)

def trapezoid_n_handler(message):
    chat_id = message.chat.id
    n = message.text
    if not n.isdigit():
        msg = bot.reply_to(message, "Number of trapezoid must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.n = n
    msg = bot.reply_to(message, "Specify trapezoid lower bound value (a)")
    bot.register_next_step_handler(msg, trapezoid_a_handler)

def trapezoid_a_handler(message):
    chat_id = message.chat.id
    a = message.text
    if not a.isdigit():
        msg = bot.reply_to(message, "Lower bound value must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.a = a
    msg = bot.reply_to(message, "Specify trapezoid upper bound value (b)")
    bot.register_next_step_handler(msg, trapezoid_b_handler)

def trapezoid_b_handler(message):
    chat_id = message.chat.id
    b = message.text
    if not b.isdigit():
        msg = bot.reply_to(message, "Upper bound value must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.b = b
    bot.send_message(chat_id, trapezoid.trapezoid_summary())
    bot.send_message(chat_id, trapezoid.calculate_trapezoid())

def trapezoid_summary_and_calculate(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, trapezoid.trapezoid_summary())
    bot.send_message(chat_id, trapezoid.calculate_trapezoid())

def trapezoid_calculate(message):
    result = trapezoid.calculate_trapezoid()
    bot.reply_to(message, result)
    bot.send_message(message, "Calculation Finished")

#running simpson handler
@bot.message_handler(commands=['simpson'])
def start_handler(message):
    msg = bot.reply_to(message, "Specify function")
    bot.register_next_step_handler(msg, simpson_function_handler)

def simpson_function_handler(message):
    chat_id = message.chat.id
    function = message.text
    shared_property.func = function
    msg = bot.reply_to(message, "Specify number of segment (n)")
    bot.register_next_step_handler(msg, simpson_n_handler)

def simpson_n_handler(message):
    chat_id = message.chat.id
    n = message.text
    if not n.isdigit():
        msg = bot.reply_to(message, "Number of trapezoid must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.n = n
    msg = bot.reply_to(message, "Specify simpson lower bound value (a)")
    bot.register_next_step_handler(msg, simpson_a_handler)

def simpson_a_handler(message):
    chat_id = message.chat.id
    a = message.text
    if not a.isdigit():
        msg = bot.reply_to(message, "Lower bound value must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.a = a
    msg = bot.reply_to(message, "Specify simpson upper bound value (b)")
    bot.register_next_step_handler(msg, simpson_b_handler)

def simpson_b_handler(message):
    chat_id = message.chat.id
    b = message.text
    if not b.isdigit():
        msg = bot.reply_to(message, "Upper bound value must be a number")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.b = b
    bot.send_message(chat_id, simpson.simpson_summary())
    bot.send_message(chat_id, simpson.calculate_simpson())

def trapezoid_summary_and_calculate(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, trapezoid.trapezoid_summary())
    bot.send_message(chat_id, trapezoid.calculate_trapezoid())

def simpson_check_bound_handler(message):
    if(simpson.n < 2):
        bot.send_message(message.chat.id, n_value_msg)
    elif(simpson.a > simpson.b):
        bot.send_message(message.chat.id, error_bound_msg)

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

print('bot start running')
bot.polling(none_stop=False)