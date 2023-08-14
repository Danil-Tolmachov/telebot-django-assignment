import os
import telebot
from dotenv import load_dotenv

import services


# Load environment variables
load_dotenv('../.env')
token = os.environ.get('BOT_TOKEN')

# Initialization
bot = telebot.TeleBot(token)
client = services.DefaultClient() # api client
user_data = {}


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

        # Get data
        data = client.get_accumulation_list(message.chat.id)
        msg_str = ''
        summary = 0

        if data is None or data == []:
            bot.send_message(message.chat.id, 'There is nothing yet')
            return

        # Item list
        for item in data:
            summary += int(item['price']) * int(item['count'])
            msg_str += services.create_item_message(item) + '\n'

        # Statistics
        msg_str += 'Sum: ' + str(summary)

        # Send message
        msg = bot.send_message(message.chat.id, msg_str)

        bot.register_next_step_handler(msg, statictic_handler)
        bot.send_message(message.chat.id, 'Send me an id to look closer')

    if message.text == 'Add':
        print(f'LOG: Add request at {message.chat.id}')
        msg = bot.send_message(message.chat.id, 'Send me some information!\n\nType(bank or anything else):')
        bot.register_next_step_handler(msg, process_type)
        

    if message.text == 'Delete':
        print(f'LOG: Delete request at {message.chat.id}')
        msg = bot.send_message(message.chat.id, 'Enter item id to delete:')
        bot.register_next_step_handler(msg, process_delete)


def statictic_handler(message):
    try:
        id = int(message.text)
    except ValueError:
        return
    
    data = client.get_accumulation(message.chat.id, id)

    if data is None:
        bot.send_message(message.chat.id, 'Something went wrong')

    msg = services.create_item_message(data)

    bot.send_message(message.chat.id, msg)
    
    


def process_type(message):
    user_data[str(message.chat.id)] = {}
    user_data[str(message.chat.id)]['type'] = message.text
    
    msg = bot.send_message(message.chat.id, 'Enter price:')
    bot.register_next_step_handler(msg, process_price)


def process_price(message):
    user_data[str(message.chat.id)]['price'] = message.text

    msg = bot.send_message(message.chat.id, 'Enter count:')
    bot.register_next_step_handler(msg, process_count)

def process_count(message):
    user_data[str(message.chat.id)]['count'] = message.text

    msg = bot.send_message(message.chat.id, 'Enter description:')
    bot.register_next_step_handler(msg, process_description)

def process_description(message):
    user_data[str(message.chat.id)]['description'] = message.text
    form = user_data[str(message.chat.id)]

    result = client.add_new_accumulation(
        message.chat.id,
        form.get('type'),
        form.get('price'),
        form.get('account_id'),
        form.get('description'),
        count = form.get('count')
    )

    del user_data[str(message.chat.id)]

    if result == False:
        bot.send_message(message.chat.id, 'Something went wrong')
    else:
        bot.send_message(message.chat.id, 'Successful!')


def process_delete(message):

    if client.delete_accumulation(message.chat.id, message.text) == True:
        bot.send_message(message.chat.id, 'Success')
    else:
        bot.send_message(message.chat.id, 'Invalid id')


if __name__ == '__main__':
    print('\n Bot has been started:')
    # Start bot
    bot.infinity_polling()
