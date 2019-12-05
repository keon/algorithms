def DFA(transitions, start, final, string):

    num = len(string)
    num_final = len(final)
    cur = start
    
    for i in range (num):
        
        if transitions[cur][string[i]] == None:
            return False
        else:
            cur = transitions[cur][string[i]]

    for i in range (num_final):
        if cur == final[i]:
            return True
        else:
            return False
        
if __name__ == "__main__":
    transitions = {
        'a': {'1': 'a', '0': 'b'},
        'b': {'1': 'b', '0': 'a'}
    }

    final=['a']
    start = 'a'
    
    print(DFA(transitions, start, final, "000111100"))
    print(DFA(transitions, start, final, "111000011"))
