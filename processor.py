def count_words(text: str) -> int:
    """
    :param text: Text to count the words in it
    :return: Sum of words in text.
    """
    parts = text.split()
    return len(parts)


def count_vowels(text: str) -> int:
    """
    Returns how many vowels are in a string.
    """
    total = 0
    for ch in text:
        if ch in "oieau":
            total = total + 1
    return total