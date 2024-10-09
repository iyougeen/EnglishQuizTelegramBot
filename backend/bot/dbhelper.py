from .models import Word, Player


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
