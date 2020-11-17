"""
Algorithm that checks if a given string is a pangram or not
"""

def check_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet:
        if ch not in input_string.lower():
            return False
    return True 