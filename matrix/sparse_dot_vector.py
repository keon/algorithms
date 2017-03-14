"""
Suppose we have very large sparse vectors, which contains a lot of zeros and double .

find a data structure to store them
get the dot product of them


In this case, we first have to store the sparse vector using hash map.
for example [3,0,0,5,6] -> (0,3) (3,5) (4,6) The key is each element's position and the value is the number.

Then we have two hash tables, and we have to iterate through them to calculate the dot product
"""
