"""
We are asked to design an efficient data structure
that allows us to add and search for words.
The search can be a literal word or regular expression
containing “.”, where “.” can be any letter.

Example:
addWord(“bad”)
addWord(“dad”)
addWord(“mad”)
search(“pad”) -> false
search(“bad”) -> true
search(“.ad”) -> true
search(“b..”) -> true
"""
import collections

class TrieNode(object):
    def __init__(self, letter, is_terminal=False):
        self.children = dict()
        self.letter = letter
        self.is_terminal = is_terminal

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode("")

    def add_word(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.is_terminal = True

    def search(self, word, node=None):
        cur = node
        if not cur:
            cur = self.root
        for i, letter in enumerate(word):
            # if dot
            if letter == ".":
                if i == len(word) - 1: # if last character
                    for child in cur.children.itervalues():
                        if child.is_terminal:
                            return True
                    return False
                for child in cur.children.itervalues():
                    if self.search(word[i+1:], child) == True:
                        return True
                return False
            # if letter
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.is_terminal

class WordDictionary2(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)


    def add_word(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
