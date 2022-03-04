from collections import defaultdict

MIN_NB_PEOPLE = 1
MAX_NB_PEOPLE = 10

"""
Check that the given caps sets is valid 

:param capsSets: The caps sets to check
:param nbCaps: The number of caps
:returns: Nothing but raises errors if invalid caps sets
"""
def check_argument(capsSets: list, nbCaps: int):
    if len(capsSets) < MIN_NB_PEOPLE or len(capsSets) > MAX_NB_PEOPLE:
        raise ValueError(f'The number of people should be {MIN_NB_PEOPLE} <= n <= {MAX_NB_PEOPLE}, but you gave {len(capsSets)} people !')
    for capsSet in capsSets:
        if not isinstance(capsSet, list):
            raise ValueError(f'The given caps set {capsSet} is not valid !')
        for cap in capsSet:
            if not isinstance(cap, int):
                raise ValueError(f'The given cap "{cap}" in caps set {capsSet} is not valid !')
            if cap > nbCaps:
                raise ValueError(f'The maximum cap id is {nbCaps}, but you gave a cap id "{cap}" in caps set {capsSet} !')

"""
Initialize the variables

:param capsSets: The caps sets given
:param nbCaps: The number of caps
:returns: The number of people, the caps dict and the DP matrix
"""
def initialization(capsSets: list, nbCaps: int):

    # check if the arguments are valid
    check_argument(capsSets, nbCaps)

    nbPeople = len(capsSets)
    nbMasks = 2 ** nbPeople

    # map each cap to its list of persons that have it
    caps = defaultdict(list)
    for person in range(nbPeople):
        for cap_id in capsSets[person]:
            caps[cap_id].append(person)

    # initialize the DP matrix
    DP = [[-1 for cap_id in range(nbCaps + 1)] for mask in range(nbMasks)]

    return nbPeople, caps, DP

"""
Determines the nr of ways to assign unique caps to current people wearing status
(i.e. current mask) having caps from cap_id to last cap to assign (or not)

:param nbPeople: The number of people
:param nbCaps: The number of caps
:param caps: The caps dict mapping each cap to its list of person that have it
:param DP: The DP matrix
:param mask: The current mask
:param cap_id: The current cap
:returns: The number of unique ways to assign unique caps
"""
def assign_unique_caps_from(nbPeople, nbCaps, caps, DP, mask, cap_id):
    
    # if the mask is full, then we found a satisfying arrangement
    if mask == (1 << nbPeople) - 1:
        return 1

    # if there are no more cap, then we did not found a satisfying arrangement
    if cap_id > nbCaps:
        return 0

    # if this subproblem is already computed, just return the solution
    if DP[mask][cap_id] != -1:
        return DP[mask][cap_id]

    # count the unique ways without taking current cap into account
    nbUniqueWays = assign_unique_caps_from(nbPeople, nbCaps, caps, DP, mask, cap_id + 1)

    if cap_id in caps:
        for person in caps[cap_id]:
            # check if the person is not already wearing a cap
            if not (mask & (1 << person)):
                # count the unique ways if the person wears the current cap
                nbUniqueWays += assign_unique_caps_from(nbPeople, nbCaps, caps, DP, mask | (1 << person), cap_id + 1)

    # store the result in the DP matrix
    DP[mask][cap_id] = nbUniqueWays

    return DP[mask][cap_id]

"""
Determines the nr of ways to assign unique caps to every person using bitmasking and dynamic programming (dp).

:param capSets: A nested list containing the caps of every person. 
:returns: The nr of ways to select unique caps for every person.
"""
def assign_unique_caps(capsSets: list, nbCaps: int) -> int:

    nbPeople, caps, DP = initialization(capsSets, nbCaps)
    
    return assign_unique_caps_from(nbPeople, nbCaps, caps, DP, 0, 1)

# For debugging purposes
def main():
    caps = [[1,2,3], [4], [1,2]]
    nbCaps = 4
    print(assign_unique_caps(caps, nbCaps))

if __name__ == '__main__':
    main()