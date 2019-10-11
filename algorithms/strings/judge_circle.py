"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a
character. The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""
def judge_circle(moves):
    dict_moves = {
        'U' : 0,
        'D' : 0,
        'R' : 0,
        'L' : 0
    }
    for char in moves:
        dict_moves[char] = dict_moves[char] + 1
    return dict_moves['L'] == dict_moves['R'] and dict_moves['U'] == dict_moves['D']
