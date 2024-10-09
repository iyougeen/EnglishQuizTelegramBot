import django
import os

from django.conf import settings

from telebot import TeleBot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'botproject.settings')

django.setup()

from bot.dbhelper import is_user_exist, register_user
from bot.tghelper import get_tg_user_data, set_commands

bot = TeleBot(settings.TELEGRAM_BOT['TOKEN'])

# Set bot commands
set_commands(bot)


# Handling /start command
@bot.message_handler(commands=['start'])
def main(message):
    if not is_user_exist(message.from_user.id):
        tg_user_data = get_tg_user_data(message)
        register_user(tg_user_data)
        welcome_message = 'Hi ' + message.chat.first_name + '! You\'re registered in English Quiz. Let\'s improve your vocabulary.'
    else:
        welcome_message = 'You\'re already registered. Send /quiz command to get quiz.'
    bot.send_message(message.chat.id, welcome_message)


# Start bot polling
bot.infinity_polling()
