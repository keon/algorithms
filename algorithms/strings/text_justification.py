'''

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
'''


def text_justification(words, maxWidth):
    '''
    :type words: list
    :type maxWidth: int
    :rtype: list
    '''
    ret=[]  #return value
    rowLen = 0  # current length of strs in a row
    rowWords = []  # current words in a row
    index = 0   # the index of current word in words
    isFirstWord = True  # is current word the first in a row
    while index < len(words):
        while rowLen <= maxWidth and index < len(words):
            if len(words[index]) > maxWidth:
                raise Exception("there exists word whose length is larger than maxWidth")
            tmp = rowLen
            rowWords.append(words[index])
            tmp += len(words[index])
            if not isFirstWord:
                tmp += 1  # except for the first word, each word should have at least a ' ' before it.
            if tmp > maxWidth:
                rowWords.pop()
                break
            rowLen = tmp
            index += 1
            isFirstWord = False
        # here we have already got a row of str , then we should supplement enough ' ' to make sure the length is maxWidth.
        row = ""
        # if the row is the last
        if index == len(words):
            for word in rowWords:
                row += (word + ' ')
            row = row[:-1]
            row += ' ' * (maxWidth - len(row))
        # not the last row and more than one word
        elif len(rowWords) != 1:
            spaceNum = maxWidth - rowLen
            spaceNumOfEachInterval = spaceNum // (len(rowWords) - 1)
            spaceNumRest = spaceNum - spaceNumOfEachInterval * (len(rowWords) - 1)
            for j in range(len(rowWords)):
                row += rowWords[j]
                if j != len(rowWords) - 1:
                    row += ' ' * (1 + spaceNumOfEachInterval)
                if spaceNumRest > 0:
                    row += ' '
                    spaceNumRest -= 1
        # row with only one word
        else:
            row+=rowWords[0]
            row+=' '*(maxWidth-len(row))
        ret.append(row)
        # after a row , reset those value
        rowLen=0
        rowWords=[]
        isFirstWord=True
    return  ret


if __name__=='__main__':
    words=["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth=16
    ret=text_justification(words,maxWidth)
    for row in ret:
        print(row)
