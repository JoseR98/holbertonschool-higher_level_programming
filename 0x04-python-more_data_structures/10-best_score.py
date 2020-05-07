#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = 0
        best_score = ''
        for i in list(a_dictionary):
            value = a_dictionary[i]
            if value > max_val:
                max_val = value
                best_score = i
        return best_score
    else:
        return None
