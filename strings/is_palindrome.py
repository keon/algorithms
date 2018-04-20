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


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s)-1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
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

"""    

# Variation 1
def string_reverse(s):
	return s[::-1]

def is_palidrome_reverse(s):
	reversed_string = string_reverse(s)

	if (s == reversed_string):
		return True
	return False	


# Variation 2
def is_palidrome_two_pointer(s):
	for i in range(0, len(s)/2):
		if (s[i] != s[len(s) - i - 1]):
			return False
	return True
	
