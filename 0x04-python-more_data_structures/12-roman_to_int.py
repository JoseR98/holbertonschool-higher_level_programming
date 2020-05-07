#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_let = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        list_num = list(roman_let[i] for i in roman_string)
        int_num = 0
        num_ones = 0
        for i in range(0, len(list_num)):
            if list_num[i] == 1:
                num_ones += 1
                int_num += list_num[i]
            else:
                if num_ones == 1 and list_num[i] != 1:
                    int_num += list_num[i] - 2
                    num_ones = 0
                else:
                    int_num += list_num[i]
        return int_num
