from common.helpers import default_compare

def sort(array, compare=default_compare):
  sorted = False
  while not sorted:
    sorted = inner_sort(array, 1, compare)
    sorted = inner_sort(array, 0, compare) and sorted
  return array

def inner_sort(array, start_i, compare):
  sorted = True
  for i in range(start_i, len(array) - 1, 2):
    if compare(array[i], array[i + 1]) > 0:
      array[i], array[i + 1] = array[i + 1], array[i]
      sorted = False
  return sorted
