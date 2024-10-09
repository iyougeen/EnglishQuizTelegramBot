from telebot import TeleBot, types, logger
from telebot.types import Message


def get_tg_user_data(message: Message) -> dict:
    """
    Get user info from TeleBot message object
    Args:
        message: TeleBot message object

    Returns:
        User info
    """
    data = {
        'tg_user_id': None,
        'tg_chat_id': None,
        'first_name': '',
        'username': '',
        'last_name': ''
    }
    if message.from_user.id:
        data['tg_user_id'] = message.from_user.id
    if message.chat.id:
        data['tg_chat_id'] = message.chat.id
    if message.from_user.first_name:
        data['first_name'] = message.from_user.first_name
    if message.from_user.username:
        data['username'] = message.from_user.username
    if message.from_user.last_name:
        data['last_name'] = message.from_user.last_name

    return data


def set_commands(bot_instance: TeleBot) -> None:
    """
    Set commands to your telegram bot
    Args:
        bot_instance: TeleBot object

    Returns:
        None
    """
    commands = [
        types.BotCommand('start', 'Start a bot'),
        types.BotCommand('quiz', 'Send me a quiz'),
    ]
    bot_instance.set_my_commands(commands)


def send_quiz(bot_instance: TeleBot, chat_id: int, poll_data: dict) -> Message:
    """
    Send a quiz (telegram poll)
    Args:
        bot_instance: TeleBot object
        chat_id: Who to send a quiz
        poll_data: Poll information to send

    Returns:
        TeleBot message object
    """
    poll_tg = bot_instance.send_poll(
        chat_id,
        poll_data['question_word'],
        poll_data['answers'],
        type='quiz',
        correct_option_id=poll_data['correct_id'],
        is_anonymous=False
    )
    return poll_tg
