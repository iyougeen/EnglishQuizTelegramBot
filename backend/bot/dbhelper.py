from .models import Word, Player, Poll
from .functions import pick_a_word, get_answers_list, get_correct_id
from telebot.types import Message
from django.utils import timezone


def is_user_exist(user_id: int) -> bool:
    """
    Check if user exists in DB or not

    Args:
        user_id: Telegram user ID

    Returns:
        True if user exists and False if not
    """
    if len(Player.objects.filter(user_id=user_id)) == 0:
        return False
    else:
        return True


def register_user(tg_user_data: dict) -> None:
    """
    Added telegram user to Player table in database
    Args:
        tg_user_data: User info

    Returns:
        None
    """
    p = Player(
        user_id=tg_user_data["tg_user_id"],
        first_name=tg_user_data["first_name"],
        username=tg_user_data["username"],
        last_name=tg_user_data["last_name"],
        num_right_answers=0,
        num_wrong_answers=0,
    )
    p.save()


def get_poll_data() -> dict:
    """
    Get information for poll
    Returns:
        All information needed for telegram poll
    """

    # Note: order_by('?') queries may be expensive and slow, depending on the database backend you’re using.
    words = list(Word.objects.order_by("?").distinct()[:3].values())

    question = pick_a_word(words)
    answers = get_answers_list(words)
    correct_id = get_correct_id(question, answers)

    poll_data = {
        "question_word": question['word'],
        "answers": answers,
        "correct_id": correct_id
    }

    return poll_data


def save_poll(poll_tg: Message) -> None:
    """
    Save information about a poll to database
    Args:
        poll_tg: Information about created poll

    Returns:
        None
    """
    p = Poll(
        poll_id=poll_tg.poll.id,
        poll_question=poll_tg.poll.question,
        poll_right_asnwer=poll_tg.poll.options[poll_tg.poll.correct_option_id].text,
        poll_right_asnwer_id=poll_tg.poll.correct_option_id,
        date_create=timezone.now()
    )
    p.save()
