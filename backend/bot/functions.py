import random


def pick_a_word(words: list[dict]) -> dict:
    """
    Random pick a word from random selected words
    Args:
        words: Random selected words from database

    Returns:
        Picked word information
    """
    words_length = len(words)
    if words_length > 0:
        random_num = random.randint(0, words_length - 1)
        return words[random_num]
    else:
        return {}


def get_answers_list(words: list[dict]) -> list[str]:
    """
    Get a list of translation selected words
    Args:
        words: Random selected words from database

    Returns:
        A list of translation
    """
    answers = []
    if words:
        for word in words:
            answers.append(word['translate'])
    return answers


def get_correct_id(question: dict, answers: list[str]) -> int:
    """
    Get an index of translated question word
    Args:
        question: A selected word information
        answers: A list of translation

    Returns:
        A number of index
    """
    if answers:
        return answers.index(question['translate'])
    else:
        return 0
