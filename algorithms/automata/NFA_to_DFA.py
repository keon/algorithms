#Code to convert an NFA to DFA. Contribution by Rahul Jyothi.
             
def NFAtoDFA(nfa,nfa_final_state):    
    new_states_list = []                          #holds all the new states created in dfa
    dfa = {}                                      #dfa dictionary/table or the output structure we needed
    keys_list = list(list(nfa.keys())[0])                  #conatins all the states in nfa plus the states created in dfa are also appended further
    path_list = list(nfa[keys_list[0]].keys())    #list of all the paths eg: [a,b] or [0,1]

###################################################

# Computing first row of DFA transition table

    dfa[keys_list[0]] = {}                        #creating a nested dictionary in dfa 
    for y in range(t):
        var = "".join(nfa[keys_list[0]][path_list[y]])   #creating a single string from all the elements of the list which is a new state
        dfa[keys_list[0]][path_list[y]] = var            #assigning the state in DFA table
        if var not in keys_list:                         #if the state is newly created 
            new_states_list.append(var)                  #then append it to the new_states_list
            keys_list.append(var)                        #as well as to the keys_list which contains all the states
        
###################################################
 
# Computing the other rows of DFA transition table

    while len(new_states_list) != 0:                     #consition is true only if the new_states_list is not empty
        dfa[new_states_list[0]] = {}                     #taking the first element of the new_states_list and examining it
        for _ in range(len(new_states_list[0])):
            for i in range(len(path_list)):
                temp = []                                #creating a temporay list
                for j in range(len(new_states_list[0])):
                    temp += nfa[new_states_list[0][j]][path_list[i]]  #taking the union of the states
                s = ""
                s = s.join(temp)                         #creating a single string(new state) from all the elements of the list
                if s not in keys_list:                   #if the state is newly created
                    new_states_list.append(s)            #then append it to the new_states_list
                    keys_list.append(s)                  #as well as to the keys_list which contains all the states
                dfa[new_states_list[0]][path_list[i]] = s   #assigning the new state in the DFA table
        
        new_states_list.remove(new_states_list[0])       #Removing the first element in the new_states_list

    print("\nDFA :- \n")    
    print(dfa)                                           #Printing the DFA created
    print("\nPrinting DFA table :- ")
    dfa_table = pd.DataFrame(dfa)
    print(dfa_table.transpose())

    dfa_states_list = list(dfa.keys())
    dfa_final_states = []
    for x in dfa_states_list:
        for i in x:
            if i in nfa_final_state:
                dfa_final_states.append(x)
                break
        
print("\nFinal states of the DFA are : ",dfa_final_states)       #Printing Final states of DFA

 

"""
# Code Ouput Example
No. of states : 4
No. of transitions : 2
state name : A
path : a
Enter end state from state A travelling through path a : 
A B
path : b
Enter end state from state A travelling through path b : 
A
state name : B
path : a
Enter end state from state B travelling through path a : 
C
path : b
Enter end state from state B travelling through path b : 
C
state name : C
path : a
Enter end state from state C travelling through path a : 
D
path : b
Enter end state from state C travelling through path b : 
D
state name : D
path : a
Enter end state from state D travelling through path a : 
path : b
Enter end state from state D travelling through path b : 
NFA :- 
{'A': {'a': ['A', 'B'], 'b': ['A']}, 'B': {'a': ['C'], 'b': ['C']}, 'C': {'a': ['D'], 'b': ['D']}, 'D': {'a': [], 'b': []}}
Printing NFA table :- 
        a    b
A  [A, B]  [A]
B     [C]  [C]
C     [D]  [D]
D      []   []
Enter final state of NFA : 
D
DFA :- 
{'A': {'a': 'AB', 'b': 'A'}, 'AB': {'a': 'ABC', 'b': 'AC'}, 'ABC': {'a': 'ABCD', 'b': 'ACD'}, 'AC': {'a': 'ABD', 'b': 'AD'}, 'ABCD': {'a': 'ABCD', 'b': 'ACD'}, 'ACD': {'a': 'ABD', 'b': 'AD'}, 'ABD': {'a': 'ABC', 'b': 'AC'}, 'AD': {'a': 'AB', 'b': 'A'}}
Printing DFA table :- 
         a    b
A       AB    A
AB     ABC   AC
ABC   ABCD  ACD
AC     ABD   AD
ABCD  ABCD  ACD
ACD    ABD   AD
ABD    ABC   AC
AD      AB    A
Final states of the DFA are :  ['ABCD', 'ACD', 'ABD', 'AD']
"""
