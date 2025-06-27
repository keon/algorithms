from collections import deque
# Trie Template for adding words checking if a prefix is valid in trie and returning list of words with that prefix
def add_word(trie, word):
    root = trie
    for c in word:
        if c not in root: root[c] = {}
        root = root[c]
    root['#'] = {}

def has_word(trie, word):
    for c in word:
        if c in trie:
            trie = trie[c]
        else: return False
    return '#' in trie

def has_prefix(trie, pre):
    for c in pre:
        if c in trie:
            trie = trie[c]
        else: return False
    return trie

def get_words_using_prefix(trie, pre):
    trie = has_prefix(trie, pre)
    if not trie: return []
    words = []
    if '#' in trie: words.append(pre)
    queue = deque([(trie, pre)])
    while queue:
        curr, pre = queue.popleft()
        for key in curr:
            temp = curr[key]
            if '#' in temp: words.append(pre + key)
            queue.append((temp, pre + key))
    return words

words = ['abcd', 'defg']
prefixes = ['a', 'def']
head = {}
for word in words:
    add_word(head, word)
for pre in prefixes:
    print(get_words_using_prefix(head, pre))