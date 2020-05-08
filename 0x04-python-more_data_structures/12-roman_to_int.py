#!/usr/bin/python3
def roman_to_int(roman_string):
    let = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    if type(roman_string) is str and roman_string:
        l = list(let[i] for i in roman_string)
        previous = 0
        for i in range(0, len(l)):
            if previous != 0 and previous < l[i]:
                int_num += l[i] - (previous * 2)
            else:
                int_num += l[i]
                previous = l[i]
    return int_num
