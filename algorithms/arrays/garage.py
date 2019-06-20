'''
We have a parking lot with exactly one empty spot. We are given two
states of the parking lot, the initial state and the final state. Both
the initial state and final state have exactly one empty spot. Both
states also have the same cars. The only difference between the states is
the arrangement of the cars.

We must determine the sequence of steps to get from the initial state to
the final state. At each step in our sequence, we are only permitted to
do one thing: we are only permitted to move some car (that is currently
in the garage) into the empty spot.

The goal is to find the shortest sequence of steps such that we rearrange
the parking lot from the initial state to the final state.

The initial state is given in the form of an array. For example:

[1, 2, 3, 0, 4]

The numbers 1, 2, 3, 4 represent different cars and 0 is the empty spot.
So the 0th garage spot contains car 1. And the 2nd garage spot contains
car 3. And the 3rd garage spot is empty.

Similarly, an example of the final state is

[0, 3, 2, 1, 4].

We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.

One sequence that is 'shortest' is

1 2 3 0 4
0 2 3 1 4
3 2 0 1 4
3 0 2 1 4
0 3 2 1 4

Another shortest sequence is

1 2 3 0 4
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4

We'll use the former strategy in garage_v1 and we'll use the latter
strategy in garage_v2.
'''

'''
Time complexity O(n^2)
Space complexity O(n)
'''
def garage_v1(initial, final, simulation=False):
    seq = [ initial[::] ]
    n = len(initial)
    assert n == len(final), 'len of initial ({}) does not equal len of final ({})'.format(n, len(final))

    d, e, f = {}, {}, {}
    for i in range(n):
        d[ initial[i] ] = i
        e[i] = initial[i]
        f[ final[i] ] = i

    def move_car_to_correct_spot(car):
        curr_pos_of_car = d[car]
        pos_car_shld_be_in = f[car]
        car_in_its_spot = e[pos_car_shld_be_in]
        curr_pos_of_zero = d[0]

        # swap zero and car_in_its_spot
        d[car_in_its_spot] = curr_pos_of_zero
        d[0] = pos_car_shld_be_in
        e[curr_pos_of_zero] = car_in_its_spot
        e[pos_car_shld_be_in] = 0
        curr_pos_of_zero, pos_car_shld_be_in = pos_car_shld_be_in, curr_pos_of_zero
        s = seq[-1][::]
        s[curr_pos_of_zero] = 0
        s[pos_car_shld_be_in] = car_in_its_spot
        seq.append(s[::])
        if car == 0: return

        # swap zero and car
        d[car] = curr_pos_of_zero
        d[0] = curr_pos_of_car
        e[curr_pos_of_zero] = car
        e[curr_pos_of_car] = 0
        curr_pos_of_zero, curr_pos_of_car = curr_pos_of_car, curr_pos_of_zero
        s[curr_pos_of_zero] = 0
        s[curr_pos_of_car] = car
        seq.append(s[::])

        # swap zero and car_in_its_spot
        d[car_in_its_spot] = curr_pos_of_zero
        d[0] = pos_car_shld_be_in
        e[curr_pos_of_zero] = car_in_its_spot
        e[pos_car_shld_be_in] = 0
        curr_pos_of_zero, pos_car_shld_be_in = pos_car_shld_be_in, curr_pos_of_zero
        s[curr_pos_of_zero] = 0
        s[pos_car_shld_be_in] = car_in_its_spot
        seq.append(s[::])
        return

    move_car_to_correct_spot(0)
    for car in d:
        if d[car] != f[car]:
            move_car_to_correct_spot(car)

    if simulation:
        assert d == f
        assert seq[-1] == final

    return seq

'''
Time complexity O(n^2)
Space complexity O(n)
'''
def garage_v2(initial, final, simulation=False):

    initial = initial[::]      # prevent changes in original 'initial'
    seq = [ initial[::] ]                   # list of each step in sequence
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):  # if zero isn't where it should be,
            car_to_move = final[zero]   # what should be where zero is,
            pos = initial.index(car_to_move)         # and where is it?
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[::])

    if simulation:
        assert seq[-1] == final

    return seq       
    # e.g.:  4, [{0, 2, 3, 1, 4}, {2, 0, 3, 1, 4}, 
    #            {2, 3, 0, 1, 4}, {0, 3, 2, 1, 4}]

"""
thus:
1 2 3 0 4 -- zero = 3, true, car_to_move = final[3] = 1,
             pos = initial.index(1) = 0, switched [0], [3]
0 2 3 1 4 -- zero = 0, f, initial[1] != final[1], switched 0,1
2 0 3 1 4 -- zero = 1, t, car_to_move = final[1] = 3,
             pos = initial.index(3) = 2, switched [1], [2]
2 3 0 1 4 -- zero = 2, t, car_to_move = final[2] = 2, 
             pos = initial.index(2) = 0, switched [0], [2]
0 3 2 1 4 -- initial == final
"""

'''
This function doesn't compute a sequence of steps. It only computes
the minimum number of steps to rearrange. But this function is much
faster.

Time complexity O(n)
Space complexity O(n)
'''
def garage_num(initial, final, simulation=False):
    n = len(initial)
    assert n == len(final)

    d, e, f = {}, {}, {}
    for i in range(n):
        d[ initial[i] ] = i
        e[i] = initial[i]
        f[ final[i] ] = i

    def move_car_to_correct_spot(car):
        curr_pos_of_car = d[car]
        pos_car_shld_be_in = f[car]
        car_in_its_spot = e[pos_car_shld_be_in]

        d[car_in_its_spot] = curr_pos_of_car
        d[car] = pos_car_shld_be_in

        e[curr_pos_of_car] = car_in_its_spot
        e[pos_car_shld_be_in] = car
        return

    move_car_to_correct_spot(0)
    j = 1
    for car in d:
        if d[car] != f[car]:
            move_car_to_correct_spot(car)
            j += 3

    if simulation: assert d == f
    return j

def test(num, initial, final, min_steps):
    seq1 = garage_v1(initial, final, simulation=True)
    seq2 = garage_v2(initial, final, simulation=True)
    r1 = len(seq1) - 1
    r2 = len(seq2) - 1
    j = garage_num(initial, final, simulation=True)
    print('test={} r1={} r2={} j={} min_steps={}\nseq1=\n{}\nseq2=\n{}'.format(num, r1, r2, j, min_steps, seq1, seq2))
    assert r1 == min_steps, 'r1={} does not equal min_steps={}'.format(r1, min_steps)
    assert r1 == r2, 'r1={} does not equal r2={}'.format(r1, r2)
    assert r1 == j, 'r1={} does not equal j={}'.format(r1, j)
    return

def main():
    test(1, [1, 3, 2, 0, 4], [0, 3, 2, 1, 4], 1)
    test(2, [1, 2, 3, 0, 4], [0, 3, 2, 1, 4], 4)
    return

if __name__ == '__main__':
    main()
