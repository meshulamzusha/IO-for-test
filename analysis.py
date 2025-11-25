from models import LineInfo


def longest_line(objs: list[LineInfo]) -> LineInfo | None:
    """
    Returns the longest line in objs.
    """
    if len(objs) == 0:
        return None

    longest = objs[0]

    for item in objs:
        if item.length > longest.length:
            longest = item

    return longest


def average_vowels(objs: list[LineInfo]) -> float:
    if len(objs) == 0:
        return 0.0

    total = 0

    for item in objs:
        total = total + item.vowels

    return total / len(objs)


def top_n_longest(objs: list[LineInfo], n: int) -> list[LineInfo]:
    sorted_objs = sorted(objs, key=lambda item: len(item.length))

    if len(objs) > n:
        return sorted_objs[::n]
    else:
        return sorted_objs