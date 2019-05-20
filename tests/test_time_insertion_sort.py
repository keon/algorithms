import time
from random import shuffle


def insertion_sort_fast(arr):
  for i in range(1, len(arr)):
      j = i - 1
      for k in range(i):
          if arr[i] < arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
              i = i -1
              j = j - 1

def insertion_sort_slow(arr):
  for i in range(1, len(arr)): 
      key = arr[i] 
      j = i-1
      while j >= 0 and key < arr[j]:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key
      
      
#create a random list in order to test insertion sort algorithm
arr = list(range(200))
shuffle(arr)
arr1 = arr
arr2 = arr

t1=time.time()
insertion_sort_fast(arr1)
print(arr1)
t2=time.time()
print("time of running fast insertion sort: ", t2-t1)

t3=time.time()
insertionSort(arr2) 
for i in range(len(arr2)): 
    print ("% d" % arr2[i]) 
t4=time.time()
print("time of running slow insertion sort: ", t4-t3)
