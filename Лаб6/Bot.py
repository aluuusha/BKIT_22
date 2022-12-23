import telebot
from telebot import types
bot = telebot.TeleBot('5989845446:AAE1QpPlNdIIjqvoHp6XwLWCh8vmhLBU2-w')
#можно было бы использовать более сложный способ хранения информации типа бд, да и этот способ не подходит,
#если ботом пользуются несколько пользователей, но задача написать бота, так что...
firNum = 0
func = ""
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите первое число:')
    bot.register_next_step_handler(message, first)
    

@bot.message_handler(content_types=['button'])
def first(message):
    global firNum
    try:
        firNum = float(message.text)
    except:
        bot.send_message(message.chat.id, 'Введите первое число:')
        bot.register_next_step_handler(message, start_message)
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.add('+', '-','*')
    markup.add('/', '%','//')
    bot.send_message(message.chat.id,'Выберите операцию:',reply_markup=markup)
    bot.register_next_step_handler(message, funct)

@bot.message_handler(commands=['text'])
def funct(message):
    global func
    func = message.text
    bot.send_message(message.chat.id, 'Введите второе число:',reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, second)

def second(message):
    global firNum, func
    try:
        secNum = float(message.text)
    except:
        bot.send_message(message.chat.id, 'Введите второе число:')
        bot.register_next_step_handler(message, second)
    bot.send_message(message.chat.id, 'Ответ: '+str(eval(str(firNum)+func+message.text)))
    bot.send_message(message.chat.id, 'Введите первое число:')
    bot.register_next_step_handler(message, first)
bot.polling()
