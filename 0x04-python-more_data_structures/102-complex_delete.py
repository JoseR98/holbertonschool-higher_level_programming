def complex_delete(a_dictionary, value):
    if value in a_dictionary:
        new = {}
        for key in a_dictionary.keys():
            if a_dictionary[key] == value:
                new[key] = a_dictionary[key]
        for key in new.keys():
            del(a_dictionary[key])
    return a_dictionary
