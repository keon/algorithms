"""
Deterministic Finite Automaton (DFA)

Simulates a DFA on an input string and determines whether the string is
accepted (ends in a final state) or rejected.

Reference: https://en.wikipedia.org/wiki/Deterministic_finite_automaton

Complexity:
    Time:  O(n) where n is the length of the input string
    Space: O(1)
"""

from __future__ import annotations


def DFA(
    transitions: dict[str, dict[str, str | None]],
    start: str,
    final: list[str],
    string: str,
) -> bool:
    """Simulate a DFA on the given input string.

    Args:
        transitions: Mapping of state -> {symbol -> next_state}.
            A value of None indicates no valid transition.
        start: The start state.
        final: A list of accepting (final) states.
        string: The input string to process.

    Returns:
        True if the string is accepted by the DFA, False otherwise.

    Examples:
        >>> transitions = {"q0": {"a": "q1", "b": None}, "q1": {"a": None, "b": "q0"}}
        >>> DFA(transitions, "q0", ["q1"], "a")
        True
        >>> DFA(transitions, "q0", ["q1"], "ab")
        False
    """
    current_state = start

    for symbol in string:
        if transitions[current_state][symbol] is None:
            return False
        current_state = transitions[current_state][symbol]

    return current_state in final
