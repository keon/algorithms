import random

my_chain = {
    'A': {'A': 0.6,
          'E': 0.4},
    'E': {'A': 0.7,
          'E': 0.3}
}

def __choose_state(state_map):
    choice = random.random()
    probability_reached = 0
    for state, probability in state_map.items():
        probability_reached += probability
        if probability_reached > choice:
            return state

def next_state(chain, current_state):
    next_state_map = chain.get(current_state)
    next_state = __choose_state(next_state_map)
    return next_state

def iterating_markov_chain(chain, state):
    while True:
        state = next_state(chain, state)
        yield state
