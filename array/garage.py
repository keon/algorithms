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
#Edited by cyberking-saga

def garage(beg, end):
    i = 0
    moves = 0
    while beg != end:
        if beg[i] != 0 and beg[i] != end[i]:
            car = beg[i]
            empty = beg.index(0)
            final_pos = end.index(beg[i])
            if empty != final_pos:
                beg[final_pos], beg[empty] = beg[empty], beg[final_pos]
                print(beg)
                empty = beg.index(0)
                beg[beg.index(car)], beg[empty] = beg[empty], beg[beg.index(car)]
                print(beg)
                moves += 2
            else:
                beg[beg.index(car)], beg[empty] = beg[empty], beg[beg.index(car)]
                print(beg)
                moves += 1
        i += 1
        if i == len(beg):
            i = 0
    return moves

if __name__ == "__main__":
    initial = [1,2,3,0,4]
    final = [0,3,2,1,4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
