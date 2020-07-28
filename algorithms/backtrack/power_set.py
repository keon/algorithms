# Python3 program to generate power set 
  
# str : Stores input string 
# curr : Stores current subset 
# index : Index in current subset, curr 
def powerSet(str1, index, curr): 
    n = len(str1) 
  
    # base case 
    if (index == n): 
        return
  
    # First print current subset 
    print(curr) 
  
    # Try appending remaining characters 
    # to current subset 
    for i in range(index + 1, n): 
        curr += str1[i] 
        powerSet(str1, i, curr) 
  
        # Once all subsets beginning with 
        # initial "curr" are printed, remove 
        # last character to consider a different 
        # prefix of subsets. 
        curr = curr.replace(curr[len(curr) - 1], "") 
  
    return
  
# Driver code 
if __name__ == '__main__': 
    str = "abc"; 
    powerSet(str, -1, "") 
  
