"""
Given a list lst and a number N, create a new list that contains each number of the list at most N times without reordering. 

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""

# Time complexity O(n^2)
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
 
# Another approach to solve the same problem using hash tables
# Run time O(n) but O(1) look up time

def delete_nth(order, max_e):
  result = [] # add the final result into this list
  my_dict = {} # keep track of occurences

  for i in order:
      if not i in my_dict:
          # first time so add it to both the dict as well as the result list
          my_dict[i] = 1  
          result.append(i)
      else:
          my_dict[i] += 1 # increment the value
          count = my_dict[i]
          # we still need to add the element if the counter is less than the number specified
          if count <= max_e:
              result.append(i)
  return result
    
    
# Some test cases
# Test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21], "From list [20,37,20,21],1 you get")
# Test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2], "From list [1,1,3,3,7,2,2,2,2],3 you get ")
# Test.assert_equals(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3), [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5], "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3 you get ")
# Test.assert_equals(delete_nth([1,1,1,1,1], 5), [1,1,1,1,1], "From list [1,1,1,1,1],5 you get ")
# Test.assert_equals(delete_nth([], 5), [], "From list [],5 you get")
