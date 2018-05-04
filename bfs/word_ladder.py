"""
Given two words (begin_word and end_word), and a dictionary's word list,
find the length of shortest transformation sequence
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
.
Note:
Return -1 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
import unittest


def ladder_length(begin_word, end_word, word_list):
    """
    Bidirectional BFS!!!
    :type begin_word: str
    :type end_word: str
    :type word_list: Set[str]
    :rtype: int
    """
    if len(begin_word) != len(end_word):
        return -1   # not possible

    if begin_word == end_word:
        return 0

    # when only differ by 1 character
    if sum(c1 != c2 for c1, c2 in zip(begin_word, end_word)) == 1:
        return 1

    begin_set = set()
    end_set = set()
    begin_set.add(begin_word)
    end_set.add(end_word)
    result = 2
    while begin_set and end_set:

        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        next_begin_set = set()
        for word in begin_set:
            for ladder_word in word_range(word):
                if ladder_word in end_set:
                    return result
                if ladder_word in word_list:
                    next_begin_set.add(ladder_word)
                    word_list.remove(ladder_word)
        begin_set = next_begin_set
        result += 1
        # print(begin_set)
        # print(result)
    return -1


def word_range(word):
    for ind in range(len(word)):
        temp = word[ind]
        for c in [chr(x) for x in range(ord('a'), ord('z') + 1)]:
            if c != temp:
                yield word[:ind] + c + word[ind + 1:]


class TestSuite(unittest.TestCase):

    def test_ladder_length(self):

        # hit -> hot -> dot -> dog -> cog
        self.assertEqual(5, ladder_length('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

        # pick -> sick -> sink -> sank -> tank == 5
        self.assertEqual(5, ladder_length('pick', 'tank',
                                          ['tock', 'tick', 'sank', 'sink', 'sick']))

        # live -> life == 1, no matter what is the word_list.
        self.assertEqual(1, ladder_length('live', 'life', ['hoho', 'luck']))

        # 0 length from ate -> ate
        self.assertEqual(0, ladder_length('ate', 'ate', []))

        # not possible to reach !
        self.assertEqual(-1, ladder_length('rahul', 'coder', ['blahh', 'blhah']))


if __name__ == '__main__':

    unittest.main()
