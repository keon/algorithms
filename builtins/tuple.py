def append_to_sequence (myseq):
    myseq += (9,9,9)
    return myseq

tuple1 = (1,2,3)     # tuples are immutable
list1  = [1,2,3]     # lists are mutable

tuple2 = append_to_sequence(tuple1)
list2  = append_to_sequence(list1)

print 'tuple1 = ', tuple1  # outputs (1, 2, 3)
print 'tuple2 = ', tuple2  # outputs (1, 2, 3, 9, 9, 9)
print 'list1  = ', list1   # outputs [1, 2, 3, 9, 9, 9]
print 'list2  = ', list2   # outputs [1, 2, 3, 9, 9, 9]
