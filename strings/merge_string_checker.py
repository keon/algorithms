"""
At a job interview, you are challenged to write an algorithm to check if a 
given string, s, can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2 are in the same 
order as in s. The interviewer gives you the following example and tells 
you to figure out the rest from the given test cases.
'codewars' is a merge from 'cdw' and 'oears':
s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


# Recursive Solution
def is_merge_recursive(s, part1, part2):
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if not s:
        return part1 + part2 == ''
    if s[0] == part1[0] and is_merge_recursive(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge_recursive(s[1:], part1, part2[1:]):
        return True
    return False


# An iterative approach
def is_merge_iterative(s, part1, part2):
    tuple_list = [(s, part1, part2)]
    while tuple_list:
        string, p1, p2 = tuple_list.pop()            
        if string:
            if p1 and string[0] == p1[0]:
                tuple_list.append((string[1:], p1[1:], p2))
            if p2 and string[0] == p2[0]:
                tuple_list.append((string[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False
