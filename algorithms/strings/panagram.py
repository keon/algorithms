"""
Given a string, check whether it is a panagram or not.

A panagram is a sentence that uses every letter at least once.

The most famous example is: "he quick brown fox jumps over the lazy dog.

Note:
A panagram in one language isn't necessarily a panagram in another. This
module assumes the english language. Hence, the Finnish panagram
'Törkylempijävongahdus' won't pass for a panagram despite being considered
a perfect panagram in its language. However, the Swedish panagram
'Yxmördaren Julia Blomqvist på fäktning i Schweiz' will pass despite
including letters not used in the english alphabet. This is because the
Swedish alphabet only extends the Latin one.
"""

from string import ascii_lowercase

def panagram(string):
    """
    Returns whether the input string is an English panagram or not.

        Parameters:
            string (str): A sentence in the form of a string.

        Returns:
            A boolean with the result.
    """
    letters = set(ascii_lowercase)
    for c in string:
        try:
            letters.remove(c.lower())
        except:
            pass
    return len(letters) == 0