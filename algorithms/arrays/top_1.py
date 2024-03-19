"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.

This algorithm gets an array, makes a dictionary of it,
 finds the most frequent count, and makes the result list.

For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

(TL:DR) Get mathematical Mode
Complexity: O(n)
"""
def top_one(array: list) -> list:
    #reserve each value which first appears on keys
    #reserve how many time each value appears by index number on values
    counting_element = dict()

    for element in array:
        if element not in counting_element.keys():
            counting_element.setdefault(element, 1)
        else:
            counting_element[element] += 1

    most_repetition_value: int = max(counting_element.values())

    return [key for key, value in counting_element.items() if value == most_repetition_value]
