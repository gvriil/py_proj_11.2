def to_uppercase(input_str):
    """: Строка в верхнем регистре.
    """
    return input_str.upper()


def capitalize_first_letters(input_str: str) -> str:
    """
    Преобразует первую букву каждого слова строки в заглавную.

    Args:
    input_str (str): Входная строка.

    Returns:
    str: Преобразованная строка.

    Пример:
    >>> capitalize_first_letters("привет мир")
    'Привет Мир'
    """

    return ' '.join(word.capitalize() for word in input_str.split())
