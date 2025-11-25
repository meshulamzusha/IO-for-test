def count_words(text: str) -> int:
    """
    :param text: Text to count the words in it
    :return: Sum of words in text.
    """
    parts = text.split()
    return len(parts)