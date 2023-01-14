"""
Given two strings s1 and s2, we are allowed to swap only one character from s1 with that of s2
such that after the swap, the total number of distinct characters in both s1 and s2 are the same.
If it is possible to perform such a swap, we should return True, else return False.

Example 1:
String 1: "cd", String 2: "e"
Expected Output: False
Explanation: On swapping the character c with e, we will end up with 2 distinct characters in string 1
and 1 character in string 2. Same goes with swapping character d with e.

Example 2:
String 1: "deff", String 2: "dde"
Expected Output: True
Explanation: We can swap character f in string 1 with character d in string 2. Hence, the new strings
will be dedf and fde. Both the string will contain three distinct characters, i.e. f, d and e.

Approach:
Create distinct prefix arrays for both string 1 and string 2. Then apply brute force to swap each of the
characters of string 1 with that of string 2 and notice if the number of distinct characters are the same.
If yes, then return True. Else, return False after all the swaps are complete.

If N is the size of string 1 and M is the size of string 2, then:

Time Complexity: O(N+M+26*26), where a complexity of N+M is required to create the prefix arrays. Also,
26*26 different swaps are required in the worst case scenario.

Space Complexity: O(26+26)=O(52) for creating the prefix arrays.
"""

# Function to create the Prefix Array.
def createPrefixArray(string):
    array,count=[0]*26,0
    for w in string:
        array[ord(w)-ord('a')]+=1
        if array[ord(w)-ord('a')]==1:
            count+=1
    return array,count

def checkSwapEquality(string1,string2):
    prefixArray1,leftCount=createPrefixArray(string1) # Time Complexity of O(N)
    prefixArray2,rightCount=createPrefixArray(string2) # Time Complexity of O(M)
    for i in range(26): # Time Complexity of O(26*26)
        if prefixArray1[i]: # Enter only if the character count is greater than 0
            prefixArray1[i]-=1
            if prefixArray1[i]==0:
                leftCount-=1
            prefixArray2[i]+=1
            if prefixArray2[i]==1:
                rightCount+=1
            for j in range(26):
                l,r=leftCount,rightCount
                if prefixArray2[j]:
                    flag=True
                    if i==j and prefixArray2[j]==1:
                        flag=False
                    if flag:
                        if prefixArray1[j]==0:
                            l+=1
                        if prefixArray2[j]==1:
                            r-=1
                        if l==r:
                            return True
            prefixArray1[i]+=1
            prefixArray2[i]-=1
            if prefixArray1[i]==1:
                leftCount+=1
            if prefixArray2[i]==0:
                rightCount-=1
    return False

