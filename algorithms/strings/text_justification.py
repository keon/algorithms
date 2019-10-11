"""
Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""


def text_justification(words, max_width):
    '''
    :type words: list
    :type max_width: int
    :rtype: list
    '''
    ret = []  # return value
    row_len = 0  # current length of strs in a row
    row_words = []  # current words in a row
    index = 0  # the index of current word in words
    is_first_word = True  # is current word the first in a row
    while index < len(words):
        while row_len <= max_width and index < len(words):
            if len(words[index]) > max_width:
                raise ValueError("there exists word whose length is larger than max_width")
            tmp = row_len
            row_words.append(words[index])
            tmp += len(words[index])
            if not is_first_word:
                tmp += 1  # except for the first word, each word should have at least a ' ' before it.
            if tmp > max_width:
                row_words.pop()
                break
            row_len = tmp
            index += 1
            is_first_word = False
        # here we have already got a row of str , then we should supplement enough ' ' to make sure the length is max_width.
        row = ""
        # if the row is the last
        if index == len(words):
            for word in row_words:
                row += (word + ' ')
            row = row[:-1]
            row += ' ' * (max_width - len(row))
        # not the last row and more than one word
        elif len(row_words) != 1:
            space_num = max_width - row_len
            space_num_of_each_interval = space_num // (len(row_words) - 1)
            space_num_rest = space_num - space_num_of_each_interval * (len(row_words) - 1)
            for j in range(len(row_words)):
                row += row_words[j]
                if j != len(row_words) - 1:
                    row += ' ' * (1 + space_num_of_each_interval)
                if space_num_rest > 0:
                    row += ' '
                    space_num_rest -= 1
        # row with only one word
        else:
            row += row_words[0]
            row += ' ' * (max_width - len(row))
        ret.append(row)
        # after a row , reset those value
        row_len = 0
        row_words = []
        is_first_word = True
    return ret
