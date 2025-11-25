def load_lines(path: str):
    """
    Reads all lines from the file and returns a list of strings without \n.
    """
    lines = []

    with open(path, "r", encoding="utf-8") as file:

        for line in file:
            cleaned = line.rstrip("\n")
            lines.append(cleaned)

    return lines


def count_lines(path: str) -> int:
    """
    Returns how many lines are in the file.
    """
    count = 0

    with open(path, "r", encoding="utf-8") as file:

        for _ in file:
            count = count + 1

    return count


def load_long_lines(path: str, min_length: int) -> list[str]:
    """
    :param path: path to file
    :param min_length: The length of all rows in the returned list will be greater than this parameter.
    :return: A list of lines whose length is greater than min_length
    """
    lines = []

    with open(path, "r", encoding="utf-8") as file:

        for line in file:
            cleaned = line.rstrip("\n")
            if len(cleaned) > min_length:
                lines.append(cleaned)

    return lines