# Following program is the python implementation of
# Rabin Karp Algorithm

class RollingHash:
    def __init__(self, text, size_word):
        self.text = text
        self.hash = 0
        self.size_word = size_word

        for i in range(0, size_word):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(size_word - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = size_word

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.size_word-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
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
    #word_hash.move_window()

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return None

