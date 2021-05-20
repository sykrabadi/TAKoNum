import telebot
from integrate import shared_property, trapezoid, simpson
from messages import messages

api_token = '<API Token Here>'
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['exit'])
def send_help(message):
    print('bot has been shutdown')
    msg = u"See you next time! \uE41E"
    bot.reply_to(message,  msg)
    #bot.polling(none_stop=True)

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

#running trapezoid handler
@bot.message_handler(commands=['trapezoid'])
def start_handler(message):
    msg = bot.reply_to(message, "Specify function")
    bot.register_next_step_handler(msg, trapezoid_function_handler)

def trapezoid_function_handler(message):    
    try:
        chat_id = message.chat.id
        function = message.text
        verify_func = lambda x: eval(str(function))
        verified_func = verify_func(0)
        shared_property.func = function
        msg = bot.reply_to(message, "Specify number of trapezoid (n)")
        bot.register_next_step_handler(msg, trapezoid_n_handler)
    except NameError:
        bot.send_message(chat_id, messages.expression_error())
        bot.register_next_step_handler(message, trapezoid_function_handler)

def trapezoid_n_handler(message):
    chat_id = message.chat.id
    n = message.text
    if not n.isdigit():
        msg = bot.reply_to(message, messages.n_value_error())
        bot.register_next_step_handler(msg, trapezoid_n_handler)
        return
    shared_property.n = n
    msg = bot.reply_to(message, "Specify trapezoid lower bound value (a)")
    bot.register_next_step_handler(msg, trapezoid_a_handler)

def trapezoid_a_handler(message):
    chat_id = message.chat.id
    a = message.text
    if not a.isdigit():
        msg = bot.reply_to(message, messages.lower_bound_error())
        bot.register_next_step_handler(msg, trapezoid_a_handler)
        return
    shared_property.a = a
    msg = bot.reply_to(message, "Specify trapezoid upper bound value (b)")
    bot.register_next_step_handler(msg, trapezoid_b_handler)

def trapezoid_b_handler(message):
    chat_id = message.chat.id
    b = message.text
    if not b.isdigit():
        msg = bot.reply_to(message, messages.upper_bound_error())
        bot.register_next_step_handler(msg, trapezoid_b_handler)
        return
    shared_property.b = b
    bot.send_message(chat_id, trapezoid.trapezoid_summary())
    bot.send_message(chat_id, trapezoid.calculate_trapezoid())
    bot.send_message(chat_id, "Calculation finished")

#running simpson handler
@bot.message_handler(commands=['simpson'])
def start_handler(message):
    msg = bot.reply_to(message, "Specify function")
    bot.register_next_step_handler(msg, simpson_function_handler)

def simpson_function_handler(message):
    try:
        chat_id = message.chat.id
        function = message.text
        verify_func = lambda x: eval(str(function))
        verified_func = verify_func(0)
        shared_property.func = function
        msg = bot.reply_to(message, "Specify number of segments (n)")
        bot.register_next_step_handler(msg, simpson_n_handler)
    except NameError:
        bot.send_message(chat_id, messages.expression_error())
        bot.register_next_step_handler(message, simpson_function_handler)

def simpson_n_handler(message):
    chat_id = message.chat.id
    n = message.text
    if not n.isdigit():
        msg = bot.reply_to(message, messages.n_value_error())
        bot.register_next_step_handler(msg, simpson_n_handler)
        return
    shared_property.n = n
    msg = bot.reply_to(message, "Specify simpson lower bound value (a)")
    bot.register_next_step_handler(msg, simpson_a_handler)

def simpson_a_handler(message):
    chat_id = message.chat.id
    a = message.text
    if not a.isdigit():
        msg = bot.reply_to(message, messages.lower_bound_error())
        bot.register_next_step_handler(msg, simpson_a_handler)
        return
    shared_property.a = a
    msg = bot.reply_to(message, "Specify simpson upper bound value (b)")
    bot.register_next_step_handler(msg, simpson_b_handler)

def simpson_b_handler(message):
    chat_id = message.chat.id
    b = message.text
    if not b.isdigit():
        msg = bot.reply_to(message, messages.upper_bound_error())
        bot.register_next_step_handler(msg, simpson_b_handler)
        return
    shared_property.b = b
    bot.send_message(chat_id, simpson.simpson_summary())
    bot.send_message(chat_id, simpson.calculate_simpson())
    bot.send_message(chat_id, "Calculation finished")

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

print('bot start running')
bot.polling(none_stop=False)