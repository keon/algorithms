# There is a parking lot with only one empty spot. Given the initial state
# of the parking lot and the final state. Each step we are only allowed to
# move a car
# out of its place and move it into the empty spot.
# The goal is to find out the least movement needed to rearrange
# the parking lot from the initial state to the final state.

# Say the initial state is an array:

# [1,2,3,0,4],
# where 1,2,3,4 are different cars, and 0 is the empty spot.

# And the final state is

# [0,3,2,1,4].
# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.


def count_moves(beg,end):
    i = 0
    count = 0
    while beg != end:
        if beg[i] != 0 and beg[i] != end[i]:
            current_car = beg[i]
            empty_slot = beg.index(0)
            final_pos = end.index(beg[i])
            if empty_slot != final_pos:
                beg[final_pos], beg[empty_slot] = beg[empty_slot], beg[final_pos]
                print beg
                empty_slot = beg.index(0)
                beg[beg.index(current_car)], beg[empty_slot] = beg[empty_slot], beg[beg.index(current_car)]
                print beg
                count += 2
            else:
                beg[beg.index(current_car)], beg[empty_slot] = beg[empty_slot], beg[beg.index(current_car)]
                print beg
                count += 1
        i += 1
        if i == len(beg):
            i = 0
    return count
                
                
initial = [1,2,3,0,4]
final = [0,3,2,1,4]
print ('Initially:',initial)
print ('Final',final)
print count_moves(initial,final)
