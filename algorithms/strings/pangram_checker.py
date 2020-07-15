def pangram_checker(text):
    # Arr is a list that contains a bool value
    # for each letter if it appeared in the sentence
    # If the entire list is true the string is a pangram.

    arr = [False] * 26

    for c in text:
        if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):

            # The character is a letter.
            c = c.lower()
            c = ord(c) - ord("a")
            arr[c] = True

    # Checking if arr is all true value

    for index in arr:
        if not index:
            return False
    return True
    
 # By Cosmos
