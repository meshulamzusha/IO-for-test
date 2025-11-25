class LineInfo:
    def __init__(self, text: str, length: int, words: int, vowels: int):
        self.text = text
        self.length = length
        self.words = words
        self.vowels = vowels


    def is_long(self) -> bool:
        """
        Returns True if the line is considered long.
        """
        return self.length > 20


    def percent_vowels(self) -> float:
        """
        Percentage of letters "oieau" out of all characters
        """
        if self.length == 0:
            return 0.0
        return (self.vowels / self.length) * 100


    def has_keyword(self, keyword: str) -> bool:
        """
        Returns True if the word appears in the text.
        """
        return keyword in self.text


    def is_dense(self) -> bool:
        """
        returns True if words < 3 and length > 25
        """
        return self.words < 3 and self.length > 25