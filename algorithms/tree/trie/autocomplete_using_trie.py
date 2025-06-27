''' In this program, text autocompletion is implemented using nested dictionary. When there are n words and for a query q,
the program returns all the words which starts qith q. i.e. q as a prefix. 
'''
from sys import stdin, stdout
END = '#'
# class that defines the basic structure of a trie with insert_word and find_word functions
class Trie:
    def __init__(self):
        self._trie = {}
    
    def insert_word(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END] = True
    
    def find_word(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return[]
        return self._elements(trie)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == END:
                subresult = [' ']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

trie = Trie()
words = ['depart', 'detergent', 'daring', 'dog', 'deer', 'deal']
for word in words:
    trie.insert_word(word)

def autocomplete_using_trie(s):
    suffixes = trie.find_word(s)
    return [s + w for w in suffixes]

def main():
    print(autocomplete_using_trie('de'))

if __name__ == "__main__":
    main()
