from models import LineInfo
from processor import count_words, count_vowels, has_keyword


def build_line_objects(lines: list[str]) -> list[LineInfo]:
    """
    Gets a list of texts, returns a list of LineInfo.
    """
    result = []

    for text in lines:
        length = len(text)
        words = count_words(text)
        vowels = count_vowels(text)
        obj = LineInfo(text, length, words, vowels)
        result.append(obj)

    return result


def build_long_only(lines: list[str], min_length: int) -> list[LineInfo]:
    """
    Gets a list of texts, returns a list of LineInfo for each long line.
    """
    result = []

    for text in lines:
        if len(text) > min_length:
            length = len(text)
            words = count_words(text)
            vowels = count_vowels(text)
            obj = LineInfo(text, length, words, vowels)
            result.append(obj)

    return result


def build_with_keyword(lines: list[str], keyword: str) -> list[LineInfo]:
    """
    Receives a list of texts,
    returns a list of LineInfo for each line containing the keyword
    """
    result = []

    for text in lines:
        if has_keyword(text, keyword):
            length = len(text)
            words = count_words(text)
            vowels = count_vowels(text)
            obj = LineInfo(text, length, words, vowels)
            result.append(obj)

    return result