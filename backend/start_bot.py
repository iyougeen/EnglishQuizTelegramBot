import django
import os

from django.conf import settings

from telebot import TeleBot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'botproject.settings')

django.setup()

from bot.dbhelper import is_user_exist, register_user, get_poll_data, save_poll, set_user_answer
from bot.tghelper import get_tg_user_data, set_commands, send_quiz

bot = TeleBot(settings.TELEGRAM_BOT['TOKEN'])

# Set bot commands
set_commands(bot)


# Handling /start command
@bot.message_handler(commands=['start'])
def main(message):
    if not is_user_exist(message.from_user.id):
        tg_user_data = get_tg_user_data(message)
        register_user(tg_user_data)
        welcome_message = 'Hi ' + message.chat.first_name + '! You\'re registered in English Quiz. Let\'s improve your vocabulary. Send /quiz command to get quiz.'
    else:
        welcome_message = 'You\'re already registered. Send /quiz command to get quiz.'
    bot.send_message(message.chat.id, welcome_message)


# Handling /quiz command
@bot.message_handler(commands=['quiz'])
def quiz(message):
    poll_data = get_poll_data()  # Prepare a poll
    poll = send_quiz(bot, message.chat.id, poll_data)  # Send a poll to telegram
    save_poll(poll)  # Save to database django


# Handling a user answer
@bot.poll_answer_handler()
def handle_poll(poll):
    set_user_answer(poll)


# Start bot polling
bot.infinity_polling()
