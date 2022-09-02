""" 
    Given a sorted unique interger array
    return summary of its range
"""

def summarize_ranges_v2(numbers):
    
    starting_index = 0
    results = []

    for i in range(len(numbers)):
        # Find last index for continuous series
        if i + 1 < len(numbers) and numbers[i] + 1 == numbers[i+1]:
            continue

        if starting_index == i:
            results.append(str(numbers[starting_index]))
        else:
            results.append(str(numbers[starting_index]) + "->" + str(numbers[i]))

        starting_index = i + 1

    return results