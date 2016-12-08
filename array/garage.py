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


def garage(beg, end):
    moves = 0
    i = 0
    while beg != end :
        if beg[i] != end[i] and beg[i] != 0:
            car = beg[i] #car that we will move
            empty = beg.index(0)
            beg[beg.index(car)], beg[empty] = beg[empty], beg[beg.index(car)]
            moves += 1
            ## move car that's not in correct place into free space
            print(beg)
            if beg.index(car) != end.index(car):
                # if the recently moved car is still not in its correct place
                # then we want to move another car into the free space where
                # it will be in its correct position
                beg[beg.index(end[i])] = 0
                beg[i] = end[i]
                print(beg)
                moves += 1
        i += 1 #move onto the next car, check again
        if i == len(beg):
            i = 0
    return moves

initial = [1,2,3,0,4]
final = [0,3,2,1,4]
print("initial:", initial)
print("final:", final)
print(garage(initial, final))
