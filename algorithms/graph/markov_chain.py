"""
Markov Chain

Provides utilities for stepping through and iterating a discrete Markov chain
described as a dictionary of transition probabilities.

Reference: https://en.wikipedia.org/wiki/Markov_chain

Complexity:
    Time:  O(S) per step, where S is the number of states
    Space: O(S)
"""

from __future__ import annotations

import random
from collections.abc import Iterator
from typing import Any


def _choose_state(state_map: dict[Any, float]) -> Any | None:
    """Choose the next state randomly according to *state_map*.

    Args:
        state_map: Mapping of state to its transition probability.

    Returns:
        The selected state, or None if probabilities don't sum to 1.
    """
    choice = random.random()
    probability_reached = 0.0
    for state, probability in state_map.items():
        probability_reached += probability
        if probability_reached > choice:
            return state
    return None


def next_state(chain: dict[Any, dict[Any, float]], current_state: Any) -> Any:
    """Return the next state given a Markov chain and current state.

    Args:
        chain: Markov chain as ``{state: {next_state: probability}}``.
        current_state: The current state.

    Returns:
        The randomly chosen next state.

    Examples:
        >>> c = {'A': {'A': 1.0}}
        >>> next_state(c, 'A')
        'A'
    """
    next_state_map = chain.get(current_state)
    return _choose_state(next_state_map)


def iterating_markov_chain(
    chain: dict[Any, dict[Any, float]],
    state: Any,
) -> Iterator[Any]:
    """Yield an infinite sequence of states from a Markov chain.

    Args:
        chain: Markov chain transition dictionary.
        state: Initial state.

    Yields:
        Successive states of the chain.
    """
    while True:
        state = next_state(chain, state)
        yield state
