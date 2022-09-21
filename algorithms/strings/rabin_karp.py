# Rabin Karp Algorithm
from string import ascii_lowercase
class RollingHash:
    def __init__(self, text, size_word):
        self.text = text
        self.hash = 0
        self.size_word = size_word
        self.mapping = dict(zip(ascii_lowercase, list(range(1, 27))))

        for i in range(0, size_word):
            self.hash += self.mapping[text[i]]*(26**(size_word - i -1))

        self.window_start = 0
        self.window_end = size_word

    def roll_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= self.mapping[self.text[self.window_start]]*26**(self.size_word-1)
            self.hash *= 26
            self.hash += self.mapping[self.text[self.window_end]]
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(word, text):
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.roll_window()
    return None

