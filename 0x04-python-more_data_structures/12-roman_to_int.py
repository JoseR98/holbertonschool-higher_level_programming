#!/usr/bin/python3
def roman_to_int(roman_string):
    let = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    if type(roman_string) is str and roman_string:
        l = list(let[i] for i in roman_string if i in let)
        num_ones = 0
        for i in range(0, len(l)):
            if l[i] == 1:
                num_ones += 1
                int_num += l[i]
            else:
                if num_ones == 1 and l[i] != 1:
                    int_num += l[i] - 2
                    num_ones = 0
                else:
                    int_num += l[i]
    return int_num
