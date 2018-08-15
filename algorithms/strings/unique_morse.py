"""
International Morse Code defines a standard encoding where each letter is mapped to
a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c"
maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
        'a':".-",
        'b':"-...",
        'c':"-.-.",
        'd': "-..",
        'e':".",
        'f':"..-.",
        'g':"--.",
        'h':"....",
        'i':"..",
        'j':".---",
        'k':"-.-",
        'l':".-..",
        'm':"--",
        'n':"-.",
        'o':"---",
        'p':".--.",
        'q':"--.-",
        'r':".-.",
        's':"...",
        't':"-",
        'u':"..-",
        'v':"...-",
        'w':".--",
        'x':"-..-",
        'y':"-.--",
        'z':"--.."

Now, given a list of words, each word can be written as a concatenation of the
Morse code of each letter. For example, "cab" can be written as "-.-.-....-",
(which is the concatenation "-.-." + "-..." + ".-"). We'll call such a
concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""

morse_code = {
    'a':".-",
    'b':"-...",
    'c':"-.-.",
    'd': "-..",
    'e':".",
    'f':"..-.",
    'g':"--.",
    'h':"....",
    'i':"..",
    'j':".---",
    'k':"-.-",
    'l':".-..",
    'm':"--",
    'n':"-.",
    'o':"---",
    'p':".--.",
    'q':"--.-",
    'r':".-.",
    's':"...",
    't':"-",
    'u':"..-",
    'v':"...-",
    'w':".--",
    'x':"-..-",
    'y':"-.--",
    'z':"--.."
}
def convert_morse_word(word):
    morse_word = ""
    word = word.lower()
    for char in word:
        morse_word = morse_word + morse_code[char]
    return morse_word

def unique_morse(words):
    unique_morse_word = []
    for word in words:
        morse_word = convert_morse_word(word)
        if morse_word not in unique_morse_word:
            unique_morse_word.append(morse_word)
    return len(unique_morse_word)
