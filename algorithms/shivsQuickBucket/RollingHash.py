# 28. Find the Index of the First Occurrence in a String

from string import ascii_lowercase
mapping = dict(zip(ascii_lowercase, list(range(1, 27))))
class RollingHash():
    def __init__(self, text, n):
        self.hash = self.w_start = 0
        self.n = self.w_end = n
        self.text = text
        self.create_hash()
    
    def create_hash(self):
        for i in range(self.n):
            self.hash += mapping[self.text[i]] * (26 ** (self.n - i - 1))
    
    def roll(self):
        if self.w_end < len(self.text):
            self.hash -= mapping[self.text[self.w_start]] * (26 ** (self.n - 1))
            self.hash *= 26
            self.hash += mapping[self.text[self.w_end]]
            self.w_start, self.w_end = self.w_start + 1, self.w_end + 1