import os
import telebot
from dotenv import load_dotenv


# Load environment variables
load_dotenv('../.env')
token = os.environ.get('BOT_TOKEN')

# Init bot
bot = telebot.TeleBot(token)


# Welcome Handler
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = "Welcome! Add new accomulations to begin"
    markup = telebot.types.ReplyKeyboardMarkup()

    statistic = telebot.types.KeyboardButton('Statistic')
    add = telebot.types.KeyboardButton('Add')
    delete = telebot.types.KeyboardButton('Delete')

    markup_row = markup.row(statistic, add, delete)

    bot.send_message(message.chat.id, text=welcome_text, reply_markup=markup)


# Button handler
@bot.message_handler(content_types=['text'])
def button_handler(message):

    if message.text == 'Statistic':
        print(f'LOG: Statistic request at {message.chat.id}')
        pass # TODO: Implement

    if message.text == 'Add':
        print(f'LOG: Add request at {message.chat.id}')
        pass # TODO: Implement

    if message.text == 'Delete':
        print(f'LOG: Delete request at {message.chat.id}')
        pass # TODO: Implement



if __name__ == '__main__':
    print('\n Bot has been started:')
    # Start bot
    bot.infinity_polling()
