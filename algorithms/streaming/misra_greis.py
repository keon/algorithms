
"""
Implementation of the Misra-Gries algorithm.
Given a list of items and a value k, it returns the every item in the list that appears at least n/k times, where n is the length of the array
By default, k is set to 2, solving the majority problem. 
For the majority problem, this algorithm only guarantees that if there is an element that appears more than n/2 times, it will be outputed. If there
is no such element, any arbitrary element is returned by the algorithm. Therefore, we need to iterate through again at the end. But since we have filtred
out the suspects, the memory complexity is significantly lower than it would be to create counter for every element in the list.

"""
def misra_gries(array,k=2):
  keys = {}
  for i in range(len(array)):
    val = str(array[i])
    if val in keys:
      keys[val] = keys[val] + 1

    elif len(keys) < k - 1:
      keys[val] = 1

    else:
      for key in list(keys):
        keys[key] = keys[key] - 1
        if keys[key] == 0:
          del keys[key]

  suspects =  keys.keys()
  frequencies = {}
  for suspect in suspects:
    freq = _count_frequency(array,int(suspect))
    if freq >= len(array) / k:
      frequencies[suspect] = freq

  return frequencies if len(frequencies) > 0 else None
  

def _count_frequency(array,element):
  return array.count(element)

if __name__ == "__main__":
  test_true = [1,4,5,4,4,5,4,4]
  test_true2 = [1,1,3,1,3,3,4,2,6,1,3]
  test_false = [1,1,3,3,2,3,4,5,6,7,8]
  print(misra_gries(test_true,3))
  print(misra_gries(test_true)))
  print(misra_gries(test_false))
      
