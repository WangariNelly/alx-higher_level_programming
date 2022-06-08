#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for element in set_1:
        if element != set_2:
            result.append(element)
    return result
 