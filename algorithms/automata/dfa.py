def DFA(transitions, start, final, string):

    num = len(string)
    num_final = len(final)
    cur = start

    for i in range(num):

        if transitions[cur][string[i]] is None:
            return False
        else:
            cur = transitions[cur][string[i]]

    for i in range(num_final):
        if cur == final[i]:
            return True
    return False
