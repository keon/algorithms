"""
Given an api which returns an array of words and an array of symbols, display
the word with their matched symbol surrounded by square brackets.

If the word string matches more than one symbol, then choose the one with
longest length. (ex. 'Microsoft' matches 'i' and 'cro'):

Example:
Words array: ['Amazon', 'Microsoft', 'Google']
Symbols: ['i', 'Am', 'cro', 'Na', 'le', 'abc']

Output:
[Am]azon, Mi[cro]soft, Goog[le]

My solution(Wrong):
(I sorted the symbols array in descending order of length and ran loop over
words array to find a symbol match(using indexOf in javascript) which
worked. But I didn't make it through the interview, I am guessing my solution
was O(n^2) and they expected an efficient algorithm.

output:
['[Am]azon', 'Mi[cro]soft', 'Goog[le]', 'Amaz[o]n', 'Micr[o]s[o]ft', 'G[o][o]gle']
"""

from functools import reduce


def match_symbol(words, symbols):
    import re
    combined = []
    for s in symbols:
        for c in words:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))
    return combined

def match_symbol_1(words, symbols):
    res = []
    # reversely sort the symbols according to their lengths.
    symbols = sorted(symbols, key=lambda _: len(_), reverse=True)
    for word in words:
        for symbol in symbols:
            word_replaced = ''
            # once match, append the `word_replaced` to res, process next word
            if word.find(symbol) != -1:
                word_replaced = word.replace(symbol, '[' + symbol + ']')
                res.append(word_replaced)
                break
        # if this word matches no symbol, append it.
        if word_replaced == '':
            res.append(word)
    return res

"""
Another approach is to use a Tree for the dictionary (the symbols), and then
match brute force. The complexity will depend on the dictionary;
if all are suffixes of the other, it will be n*m
(where m is the size of the dictionary). For example, in Python:
"""


class TreeNode:
    def __init__(self):
        self.c = dict()
        self.sym = None


def bracket(words, symbols):
    root = TreeNode()
    for s in symbols:
        t = root
        for char in s:
            if char not in t.c:
                t.c[char] = TreeNode()
            t = t.c[char]
        t.sym = s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, t = i, root
            while j < len(word) and word[j] in t.c:
                t = t.c[word[j]]
                if t.sym is not None:
                    symlist.append((j + 1 - len(t.sym), j + 1, t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1] - x[0] >= y[1] - y[0] else y,
                         symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2],
                                             word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)
