"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.
"""
from string import ascii_letters


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s)-1
    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1
    return True

"""
Here is a bunch of other variations of is_palindrome function.

Variation 1:
Find the reverse of the string and compare it with the original string

Variation 2:
Loop from the start to length/2 and check the first character and last character
and so on... for instance s[0] compared with s[n-1], s[1] == s[n-2]...

Variation 3:
Using stack idea. 

Note: We are assuming that we are just checking a one word string. To check if a complete sentence 
"""  
def remove_punctuation(s):
    """
    Remove punctuation, case sensitivity and spaces
    """
    return "".join(i.lower() for i in s if i in ascii_letters)

# Variation 1
def string_reverse(s):
	return s[::-1]

def is_palindrome_reverse(s):
	s = remove_punctuation(s)
	
	# can also get rid of the string_reverse function and just do this return s == s[::-1] in one line.
	if (s == string_reverse(s)): 
		return True
	return False	


# Variation 2
def is_palindrome_two_pointer(s):
    s = remove_punctuation(s)
	
    for i in range(0, len(s)//2):
        if (s[i] != s[len(s) - i - 1]):
            return False
    return True
	

# Variation 3
def is_palindrome_stack(s):
    stack = []
    s = remove_punctuation(s)
	
    for i in range(len(s)//2, len(s)):
        stack.append(s[i])
    for i in range(0, len(s)//2):
        if s[i] != stack.pop():
            return False
    return True	
