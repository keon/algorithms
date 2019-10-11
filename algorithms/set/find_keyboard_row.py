"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard.

For example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Reference: https://leetcode.com/problems/keyboard-row/description/
"""
def find_keyboard_row(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    keyboard = [
        set('qwertyuiop'),
        set('asdfghjkl'),
        set('zxcvbnm'),
    ]
    result = []
    for word in words:
        for key in keyboard:
            if set(word.lower()).issubset(key):
                result.append(word)
    return result
