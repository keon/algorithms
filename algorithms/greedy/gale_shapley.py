"""
Gale-Shapley Stable Matching

Solves the stable matching (stable marriage) problem. Given N men and N women
with ranked preferences, produces a stable matching where no pair would prefer
each other over their current partners.

Reference: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations


def gale_shapley(
    men: dict[str, list[str]],
    women: dict[str, list[str]],
) -> dict[str, str]:
    """Find a stable matching between men and women.

    Args:
        men: Mapping of each man to his preference list of women
            (highest to lowest).
        women: Mapping of each woman to her preference list of men
            (highest to lowest).

    Returns:
        A dict mapping each man to his matched woman.

    Examples:
        >>> men = {"M1": ["W1", "W2"], "M2": ["W1", "W2"]}
        >>> women = {"W1": ["M2", "M1"], "W2": ["M1", "M2"]}
        >>> sorted(gale_shapley(men, women).items())
        [('M1', 'W2'), ('M2', 'W1')]
    """
    men_available: list[str] = list(men.keys())
    married: dict[str, str] = {}
    proposal_counts: dict[str, int] = {man: 0 for man in men}

    while men_available:
        man = men_available.pop(0)
        woman = men[man][proposal_counts[man]]
        proposal_counts[man] += 1

        if woman not in married:
            married[woman] = man
        else:
            current_partner = married[woman]
            if women[woman].index(man) < women[woman].index(current_partner):
                married[woman] = man
                men_available.append(current_partner)
            else:
                men_available.append(man)

    return {man: woman for woman, man in married.items()}
