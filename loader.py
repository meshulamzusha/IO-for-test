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
