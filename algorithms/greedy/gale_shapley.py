"""
The Gale-Shapley algorithm is a method to solve the
stable matching/marriage problem. Given N men and women
with ranked preferences of the opposite sex, the men and
women will be matched so that each pair of man and woman
would not prefer someone over their current match. With
no conflicting preferences, the matches are stable. The
algorithm can be extended to issues that involve ranked
matching.

Example for function:
    M denotes man, W denotes woman, and number corresponds to
    respective man/woman. Preference lists go from highest to lowest.

    men_preferences = {
        "M1": ["W1", "W2", "W3"],
        "M2": ["W1", "W3", "W2"],
        "M3": ["W3", "W1", "W2"],
    }
    women_preferences = {
        "W1": ["M2", "M1", "M3"],
        "W2": ["M1", "M2", "M3"],
        "W3": ["M3", "M1", "M2"],
    }

    input: print(gale_shapley(men_preferences, women_preferences))
    output: {'M2': 'W1', 'M3': 'W3', 'M1': 'W2'}
    Explanation:
        Both Man 1 and Man 2 have a top preference of Woman 1,
        and since Woman 1 has a top preference of Man 2, Man 2
        and Woman 1 are matched, and Man 1 is added back to available
        men. Man 3 and Woman 3 have their top preference as each other,
        so the two are matched. Man 1 then proposes to Woman 2, and
        Man 1 is the top preference of Woman 2, so the two are matched.
        There is no match of Man AND Woman where both would want to
        leave, so the current matches are stable.

"""

# size denotes the number of men/women
# Function takes in dictionary for men and women preferences in style outlined above
def gale_shapley(men, women):
    size = len(men)
    # Initialize all men to be available
    men_available = list(men.keys())
    # Initialize married to empty
    married = {}
    # Intialize proposal count for each man to 0
    proposal_counts = {man: 0 for man in men}
    while men_available:
        # Pop first available man
        man = men_available.pop(0)
        # Of the popped man, set woman equal to corresponding proposal index
        woman = men[man][proposal_counts[man]]
        #increment proposal count
        proposal_counts[man] += 1
        if woman not in married:
            # Set marriage if woman not married
            married[woman] = man
        else:
            # If woman married, currently_married corresponds to currently matched man
            currently_married = married[woman]
            if women[woman].index(man) < women[woman].index(currently_married):
                """
                If the available man is of greater preference to the woman than her
                currently married partner, change the marriage to the new available
                man and append the previously married man back to men_available
                """
                married[woman] = man
                men_available.append(currently_married)
            else:
                # Add man back to men_available and try woman at next index
                men_available.append(man)
    # Returns pairs of matched men and women in form of Man:Woman
    return {man: woman for woman, man in married.items()}

# Example case
men_preferences = {
    "M1": ["W1", "W2", "W3"],
    "M2": ["W1", "W3", "W2"],
    "M3": ["W3", "W1", "W2"],
}
women_preferences = {
    "W1": ["M2", "M1", "M3"],
    "W2": ["M1", "M2", "M3"],
    "W3": ["M3", "M1", "M2"],
}

res = gale_shapley(men_preferences, women_preferences)
print(res)