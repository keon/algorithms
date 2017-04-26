"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.

eg: for given string -> "appletablet"
"apple", "tablet"
"applet", "able", "t"
"apple", "table", "t"
"app", "let", "able", "t"

"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1
"""

count = 0

def make_sentence(str_piece, dictionarys):
    global count
    if len(str_piece) == 0:
        return True
    for i in range(0, len(str_piece)):
        prefix, suffix = str_piece[0:i], str_piece[i:]
        if ((prefix in dictionarys and suffix in dictionarys)
                or (prefix in dictionarys
                    and make_sentence(suffix, dictionarys))):
            count += 1
    return True


if __name__ == "__main__":
    dictionarys = ["", "app", "let", "t", "apple", "applet"]
    word = "applet"
    make_sentence(word, dictionarys)
    print count