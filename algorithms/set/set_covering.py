from itertools import chain, combinations

"""
Universe *U* of n elements
Collection of subsets of U:
    S = S1,S2...,Sm
    Where every substet Si has an associated cost.

Find a minimum cost subcollection of S that covers all elements of U

Example:
    U = {1,2,3,4,5}
    S = {S1,S2,S3}

    S1 = {4,1,3},    Cost(S1) = 5
    S2 = {2,5},      Cost(S2) = 10
    S3 = {1,4,3,2},  Cost(S3) = 3

    Output:
        Set cover = {S2, S3}
        Min Cost = 13
"""


def powerset(iterable):
    """Calculate the powerset of any iterable.

    For a range of integers up to the length of the given list,
    make all possible combinations and chain them together as one object.
    From https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def optimal_set_cover(universe, subsets, costs):
    """ Optimal algorithm - DONT USE ON BIG INPUTS - O(2^n) complexity!
    Finds the minimum cost subcollection os S that covers all elements of U

    Args:
        universe (list): Universe of elements
        subsets (dict): Subsets of U {S1:elements,S2:elements}
        costs (dict): Costs of each subset in S - {S1:cost, S2:cost...}
    """
    pset = powerset(subsets.keys())
    best_set = None
    best_cost = float("inf")
    for subset in pset:
        covered = set()
        cost = 0
        for s in subset:
            covered.update(subsets[s])
            cost += costs[s]
        if len(covered) == len(universe) and cost < best_cost:
            best_set = subset
            best_cost = cost
    return best_set


def greedy_set_cover(universe, subsets, costs):
    """Approximate greedy algorithm for set-covering. Can be used on large
    inputs - though not an optimal solution.

    Args:
        universe (list): Universe of elements
        subsets (dict): Subsets of U {S1:elements,S2:elements}
        costs (dict): Costs of each subset in S - {S1:cost, S2:cost...}
    """
    elements = set(e for s in subsets.keys() for e in subsets[s])
    # elements don't cover universe -> invalid input for set cover
    if elements != universe:
        return None

    # track elements of universe covered
    covered = set()
    cover_sets = []

    while covered != universe:
        min_cost_elem_ratio = float("inf")
        min_set = None
        # find set with minimum cost:elements_added ratio
        for s, elements in subsets.items():
            new_elements = len(elements - covered)
            # set may have same elements as already covered -> new_elements = 0
            # check to avoid division by 0 error
            if new_elements != 0:
                cost_elem_ratio = costs[s] / new_elements
                if cost_elem_ratio < min_cost_elem_ratio:
                    min_cost_elem_ratio = cost_elem_ratio
                    min_set = s
        cover_sets.append(min_set)
        # union
        covered |= subsets[min_set]
    return cover_sets


if __name__ == '__main__':
    universe = {1, 2, 3, 4, 5}
    subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}
    costs = {'S1': 5, 'S2': 10, 'S3': 3}

    optimal_cover = optimal_set_cover(universe, subsets, costs)
    optimal_cost = sum(costs[s] for s in optimal_cover)

    greedy_cover = greedy_set_cover(universe, subsets, costs)
    greedy_cost = sum(costs[s] for s in greedy_cover)

    print('Optimal Set Cover:')
    print(optimal_cover)
    print('Cost = %s' % optimal_cost)

    print('Greedy Set Cover:')
    print(greedy_cover)
    print('Cost = %s' % greedy_cost)
