import os
import telebot

# Get token from environment
token = os.environ.get('BOT_TOKEN')


# Init bot
bot = telebot.TeleBot(token)


if __name__ == '__main__':
    # Start bot
    bot.infinity_polling()
